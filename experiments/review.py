#!/usr/bin/env python3
"""
review.py — Run ChatGPT and Gemini reviews in parallel against repo context.

Usage:
    python experiments/review.py --context ai-dev-workflow/README.md --type both
    python experiments/review.py --context ai-dev-workflow/README.md --type architecture
    python experiments/review.py --context README.md --plan "Add a CLI tool for mood mapping" --output reviews/output.txt

Requires: OPENAI_API_KEY and GEMINI_API_KEY in a root .env file.
"""

import argparse
import os
import sys
import threading
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def read_context_files(paths: list) -> str:
    parts = []
    for path in paths:
        p = Path(path)
        if not p.exists():
            print(f"Warning: file not found: {path}", file=sys.stderr)
            continue
        parts.append(f"--- {path} ---\n{p.read_text()}")
    return "\n\n".join(parts)


def build_chatgpt_prompt(project: str, context: str, plan: str) -> str:
    plan_section = plan if plan else "(no specific plan — review the project context above)"
    return f"""Review this Claude Code implementation plan as an external architecture, product, and roadmap reviewer.

Project:
{project}

Current state:
{context}

Claude plan:
{plan_section}

Review for:
- product value
- architecture quality
- maintainability
- implementation risk
- missing edge cases
- over-engineering
- roadmap alignment

Give me:
- approve / approve with changes / reject
- what is strong
- what should change before implementation
- edge cases
- acceptance criteria
- test commands
- whether this should be built now"""


def build_gemini_prompt(project: str, target_user: str, context: str) -> str:
    return f"""Review this project idea or feature as an external UX, product, and usefulness reviewer.

Project:
{project}

Target user:
{target_user}

Current idea or feature:
{context}

Review for:
- usefulness
- clarity
- user experience
- onboarding
- product potential
- what might confuse users
- what should be simplified
- what would make this more valuable

Give me:
- overall assessment
- strengths
- weaknesses
- missing pieces
- suggested improvements
- product opportunities
- best next step"""


def run_chatgpt(prompt: str, results: dict) -> None:
    try:
        import openai
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        results["chatgpt"] = response.choices[0].message.content
    except Exception as e:
        results["chatgpt"] = f"Error calling ChatGPT: {e}"


def run_gemini(prompt: str, results: dict) -> None:
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        results["gemini"] = response.text
    except Exception as e:
        results["gemini"] = f"Error calling Gemini: {e}"


def format_section(title: str, content: str) -> str:
    divider = "=" * 60
    return f"{divider}\n{title}\n{divider}\n{content}"


def main():
    parser = argparse.ArgumentParser(
        description="Run ChatGPT and Gemini reviews in parallel against repo context."
    )
    parser.add_argument(
        "--context", nargs="+", default=[],
        help="One or more file paths to include as context (e.g. README.md ai-dev-workflow/README.md)"
    )
    parser.add_argument(
        "--type", choices=["architecture", "ux", "both"], default="both",
        help="architecture = ChatGPT only, ux = Gemini only, both = run both (default)"
    )
    parser.add_argument(
        "--project", default="builtbytoobai/creative-ai-experiments",
        help="Project name to include in the review prompt"
    )
    parser.add_argument(
        "--user", default="developer or creator exploring AI-assisted tools",
        help="Target user description for the Gemini UX prompt"
    )
    parser.add_argument(
        "--plan", default="",
        help="Optional: paste Claude's implementation plan here to include in the architecture review"
    )
    parser.add_argument(
        "--output", default="",
        help="Optional: save the full review output to this file path"
    )
    args = parser.parse_args()

    if not args.context and not args.plan:
        print("Error: provide at least --context <file> or --plan <text>", file=sys.stderr)
        sys.exit(1)

    context = read_context_files(args.context) if args.context else ""

    run_arch = args.type in ("architecture", "both")
    run_ux = args.type in ("ux", "both")

    if run_arch and not OPENAI_API_KEY:
        print("Error: OPENAI_API_KEY not set. Copy .env.example to .env and add your key.", file=sys.stderr)
        sys.exit(1)

    if run_ux and not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY not set. Copy .env.example to .env and add your key.", file=sys.stderr)
        sys.exit(1)

    results = {}
    threads = []

    if run_arch:
        prompt = build_chatgpt_prompt(args.project, context, args.plan)
        threads.append(threading.Thread(target=run_chatgpt, args=(prompt, results)))

    if run_ux:
        prompt = build_gemini_prompt(args.project, args.user, context)
        threads.append(threading.Thread(target=run_gemini, args=(prompt, results)))

    print(f"Running {'ChatGPT + Gemini' if len(threads) > 1 else ('ChatGPT' if run_arch else 'Gemini')} review(s) in parallel...\n")

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    output_sections = []

    if "chatgpt" in results:
        section = format_section("CHATGPT REVIEW (Architecture / Product)", results["chatgpt"])
        output_sections.append(section)
        print(section)
        print()

    if "gemini" in results:
        section = format_section("GEMINI REVIEW (UX / Usefulness)", results["gemini"])
        output_sections.append(section)
        print(section)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("\n\n".join(output_sections))
        print(f"\nReview saved to: {args.output}")


if __name__ == "__main__":
    main()

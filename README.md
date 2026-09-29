# debugging-dojo

A truthful record of learning to debug software and AI systems: wrong turns included.

## Why this exists

AI tools can write code faster than I can. What they can't give me is the ability to
stay calm and methodical when that code breaks. This repo is where I train that skill,
one bug at a time, and keep an honest record of how I think while doing it.

## Rules of this repo

1. **Commit the broken code first**, exactly as received, before touching anything.
2. **Commit while investigating**: logging I added, hypotheses I tested, dead ends.
   The history should show the process, not just the fix.
3. **No AI solving the drills.** AI can explain a concept *after* I've made a real attempt,
   and that gets written down in the post-mortem too.
4. **Wrong hypotheses stay in the post-mortem.** They are the most useful part.
5. **Nothing gets cleaned up to look smarter than it was.**

## The path

| Stage | Focus |
|-------|-------|
| 1 | Debugging method on plain Python: stack traces, breakpoints, isolating bugs |
| 2 | The layers underneath: HTTP, APIs, rate limits, env vars, dependencies |
| 3 | RAG and an agent built by hand, no frameworks |
| 4 | Observability and evals: tracing every LLM call, a small eval set |
| 5 | Chaos drills: hidden faults, diagnosed from logs and traces only |
| 6 | Working with AI coding tools: reviewing and questioning AI-written code |
| 7 | Final exam: return to Chaos-RAG, an earlier project I built without fully understanding it, and write an honest post-mortem of it |

Stage 1 is separate drills. **Stages 2–5 build one system that grows over time**: a small
LLM service, then retrieval and an agent loop, then tracing and evals, then a fault injector
that breaks it on purpose. Every layer is written and understood before the next one starts.

Plus `incidents/`: write-ups of simulated production incidents.

## Progress

| Drill | Stage | Minutes to root cause | Root cause (one line) |
|-------|-------|-----------------------|-----------------------|
| 01 | 1 | | |

## Files

- `PLAYBOOK.md`: patterns I've learned, added only when I've seen them for real
- `POSTMORTEM_TEMPLATE.md`: copied into every drill folder

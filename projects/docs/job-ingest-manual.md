# Job Ingest Manual

## Purpose

Turn a saved job page into a structured local note without relying on manual retyping or full AI extraction.

The workflow is intentionally semi-manual:

- save the job page HTML
- run the local ingest script
- review the extracted result
- file the note in the jobs system

This keeps the process fast while avoiding browser automation or LinkedIn login automation.

## Files

- Ingest script: [`/home/jman/engineering-codex/scripts/job_ingest.py`](/home/jman/engineering-codex/scripts/job_ingest.py)
- Wrapper command: [`/home/jman/engineering-codex/scripts/job_ingest`](/home/jman/engineering-codex/scripts/job_ingest)
- New-job template: [`/home/jman/engineering-codex/jobs/new-job.md`](/home/jman/engineering-codex/jobs/new-job.md)
- Skill tracker: [`/home/jman/engineering-codex/projects/career-skill-tracker.md`](/home/jman/engineering-codex/projects/career-skill-tracker.md)

## Inputs

You need:

- a saved LinkedIn job HTML file
- the job URL
- optionally, a note filename for the final markdown output

## Save the Job Page

Save the job page manually from the browser as HTML.

Recommended:

- save the page after opening the full posting
- keep the filename stable and readable
- store it in `projects/jobs/` for raw captures

## Run the Ingest

Use the wrapper command:

```bash
/home/jman/engineering-codex/scripts/job_ingest \
  --html '/home/jman/engineering-codex/projects/jobs/Integration_Engineer_Access_Information_Management_LinkedIn.html' \
  --url 'https://www.linkedin.com/jobs/view/4443049539/' \
  --out '/tmp/job-summary.md'
```

If you omit `--out`, the script writes a `.md` file next to the HTML file automatically.

If you want stdout instead of a file:

```bash
/home/jman/engineering-codex/scripts/job_ingest \
  --html '/home/jman/engineering-codex/projects/jobs/Integration_Engineer_Access_Information_Management_LinkedIn.html' \
  --url 'https://www.linkedin.com/jobs/view/4443049539/'
```

## What the Script Does

- extracts a job header from the saved HTML
- pulls a rule-based skill list from the posting text
- matches the job against the current experience buckets
- writes a markdown summary if `--out` is provided

## Review Step

Always check the generated output before filing it.

Verify:

- company name
- role title
- location
- compensation, if present
- extracted skills
- matched experience

If the header looks wrong, the HTML export is probably noisy or incomplete. Re-save the page and try again.

## File the Job Note

After review, create or update a job note under `jobs/`.

Suggested flow:

1. Copy [`jobs/new-job.md`](/home/jman/engineering-codex/jobs/new-job.md)
2. Fill in the job-specific fields
3. Paste the extracted skill list and experience matches
4. Add a fit score and target / maybe / skip decision

## Update the Skill Tracker

If the job adds a new repeated skill, update:

- [`/home/jman/engineering-codex/projects/career-skill-tracker.md`](/home/jman/engineering-codex/projects/career-skill-tracker.md)
- [`/home/jman/engineering-codex/projects/career-acceleration.md`](/home/jman/engineering-codex/projects/career-acceleration.md)

Only increase counts when the skill actually appears in another reviewed job.

## Rules

- Do not automate LinkedIn login or aggressive scraping.
- Do not trust the first pass blindly.
- Keep the human review step.
- Use the script as a helper, not as the source of truth.

## Quick Checklist

- [ ] save the job HTML
- [ ] run `scripts/job_ingest`
- [ ] review the summary
- [ ] file the job note
- [ ] update the skill tracker if needed
- [ ] commit the change

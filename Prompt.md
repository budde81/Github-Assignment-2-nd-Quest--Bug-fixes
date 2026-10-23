# Prompt for This Folder

## Project Overview
This folder contains a small Python Selenium automation task. The goal is to create or repair a script that opens Google, searches for "Python Selenium", waits for the results page, and exits cleanly without leaving a browser session running.

## Main Files
- `confest.py` — the Selenium script to fix or improve
- `requirements.txt` — project dependency list (includes `selenium==4.51.0`)
- `quality_improvements.txt` — expected quality improvements for the final implementation
- `selenium_code_bugs.txt` — known defects that must be avoided in the final fix
- `pyrightconfig.json` — static type-check configuration
- `.github/workflows/python-checks.yml` — CI workflow that runs type checks with Pyright

## Objective
Implement the corrected version of the Selenium automation in `confest.py` so that it:

- uses the correct Google search field locator (`name="q"`)
- waits for page state changes using `WebDriverWait` instead of arbitrary sleeps
- handles Google verification pages gracefully instead of treating them as search results
- closes the browser with `driver.quit()` in a `try/finally` block
- avoids runtime errors such as `AttributeError` from `driver.titel`
- keeps the script modular and readable with `main()` and a proper `if __name__ == "__main__":` guard

## Important Constraints
- Do not bypass Google’s verification or anti-bot protections.
- Treat the browser verification page as a legitimate condition that should be handled explicitly.
- Prefer explicit waits for page readiness and DOM presence over fixed `sleep()` delays.
- Keep the search query in one place and reuse it consistently.
- Preserve a clear, structured entry point and clean imports.

## Expected Quality Improvements
The final solution should reflect the improvements described in `quality_improvements.txt`, including:

- correct locator usage
- explicit waits instead of fixed delays
- reliable WebDriver cleanup
- clear handling of Google verification
- modular structure with `main()`
- single source of truth for the search query
- readable imports and type annotation

## Known Bugs to Avoid
The final implementation must not reintroduce the issues listed in `selenium_code_bugs.txt`, including:

- wrong search locator (`q1`)
- typoed property access (`driver.titel`)
- use of fixed `sleep()` instead of waiting for page conditions
- failing to close the browser when exceptions occur
- using `driver.close()` instead of `driver.quit()`
- stray unusual whitespace that could cause syntax issues

## Validation
After making the fix, validate with the project tools already configured:

1. Install dependencies:
   `python -m pip install -r requirements.txt`
2. Run static type checks:
   `pyright`
3. If browser automation is run locally, confirm the script opens Google, submits the query, waits for results, and exits without leaving a process behind.

## Success Criteria
The task is complete when:
- `confest.py` is functionally correct and robust
- the project passes Pyright checks
- the implementation matches the quality improvements listed in the repository
- the known Selenium bugs are not present in the final code

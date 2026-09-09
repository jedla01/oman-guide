# Content guidelines

- Keep the guide concise and in Czech. Lead with the important information.
- Use Oman's flag and its red, white and green colors for the visual style. Prefer bright white surfaces and readable contrast; avoid desert, sand and brown styling.
- Use tables for structured facts such as flights, fares, accommodation and budgets. Do not add long descriptions or repeat table values in prose.
- For flights, show dates, flight numbers, airports, departure and arrival times, durations, connections and prices with currency. Mark next-day arrivals clearly.
- Highlight the preferred option (currently Saver for flights) and show totals. Put direction-level fares once per direction, not on every flight segment.
- Add short notes only when needed to explain an ambiguity, discrepancy or booking status. Do not invent missing details or treat selected options as booked.
- Keep detailed information on one page and link to it from the overview and relevant days.
- Edit source files in `docs/`; do not edit generated `_site/` output.
- Preserve Jekyll front matter. New navigation pages need `layout`, `title`, a unique `permalink` and `nav_order`. Use `relative_url` for internal links.
- For content edits, check Markdown tables, links and `git diff --check`. No new tests are needed for simple text changes.

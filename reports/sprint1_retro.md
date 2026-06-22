# Sprint 1 Retrospective

## Objectives Completed

- Project structure created
- Python virtual environment configured
- Dependencies installed
- Excel loader developed
- Ticker normalization implemented
- Year normalization implemented
- Unit tests created and passed
- Data validator developed
- Validation report generated
- SQLite database schema created
- Core datasets loaded
- Supporting datasets loaded
- Load audit generated
- Data quality review completed
- Exploratory SQL queries written

## Challenges Faced

- Excel files required header=1 loading.
- Year formats varied across datasets.
- Foreign key failures occurred due to company ticker mismatches.
- Some datasets contained duplicate company-year combinations.
- SQLite module execution required package-based imports.

## Lessons Learned

- Normalize data before loading.
- Validate datasets early.
- Use automated tests for utility functions.
- Check foreign key consistency before database loading.

## Sprint Outcome

Sprint 1 successfully completed.

Database contains all required datasets and is ready for analytics development in Sprint 2.
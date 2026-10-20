
3. Install Python 3 if needed, then run:
   ```powershell
   python -m pip install pandas jupyter nbconvert
   ```
4. Run the analysis:
   ```powershell
   python src\analysis.py
   ```
5. Open the notebook:
   ```powershell
   jupyter notebook
   ```
   In the browser, open `notebooks/analysis.ipynb` and choose **Run All**.
6. Export the notebook to Python from the project root:
   ```powershell
   jupyter nbconvert --to script notebooks/analysis.ipynb
   ```
   Move the generated `notebooks/analysis.py` into `src` if you want to keep the export there.


## Five-line summary of findings

1. The department dataset contains five departments.
2. The total department budget is 930,000.
3. IT has the highest budget at 300,000.
4. Marketing has the lowest budget at 100,000.
5. Employee counts and city counts are generated from the employee CSV.

## Git / GitHub checklist

- Create a repository named `week1-assessment`.
- Use branch `feature/analysis`.
- Make at least five small commits with clear messages.
- Search for Chennai in Git Bash using `grep -in "Chennai" data/*.csv`.
- Open a Pull Request into `main`, resolve a deliberate README conflict, and merge.
- Capture `git log --oneline --graph --all` and submit the screenshot plus the real PR URL.

## Assessment Progress
- Added analysis workflow and department budget summary.

<<<<<<< HEAD
## Pull Request Update
Feature branch analysis documentation.

Feature branch note: Employee city analysis.
=======
Main branch note: Department budget analysis.
>>>>>>> main

This repo will be used for demoing Thursday learning sessions

Create a new github workflow that meets the below requirements. A good starting point is looking at the github quickstart page https://docs.github.com/en/actions/quickstart, and opening our dashboards repository to see how they have been implemented there.
- It must run when a pull request is created / updated
- It must contain a job that prints the lyrics using the lyrics.py file
    - Hint - https://github.com/actions/setup-python
- It must contain a job that adds a random chuck norris quote as a comment to pull requests
    - Hint -https://github.com/Marta83/funny-comment-action

Bonus:
- Create a new unit test file, and add a test that will always fail
- Add a new job to your workflow that runs this unit test
    - Hint - You won't have pytest installed without a conda environment, but you can install pip packages inside a github action using a python command
- Change the job that adds a chuck norris quote to only run when the unit test job succeeds
    - Hint - https://docs.github.com/en/actions/using-workflows/about-workflows#creating-dependent-jobs
- Fix the unit test, enjoy another chuck norris quote
# Helpful Git Commands

This contains very helpful `git` commands for reference.

If you are not already in the project directory, always run this before doing anything else.
```bash
$ cd PROJECT DIRECTORY
$ git remote add origin https://<OTP TOKEN>@<GITHUB REPO LINK>
```
In particular, replace `PROJECT DIRECTORY` with the project directory file name,  `OTP TOKEN` with the OTP Token given by GitHub, and `GITHUB REPO LINK` with the actual GitHub repository link.

## Erasing Entire Commit History
In order to erase all previous commit history on the branch `main` of the GitHub repository both locally and remotely, run the following git commands:
```bash
$ git checkout --orphan latest_branch
$ git add -A
$ git commit -am "commit message"
$ git branch -D main
$ git branch -m main
$ git push -f origin main
```

## Version Control Tags
Tags are useful for version control. To add a tag named `tagname`,
```bash
$ git tag <tagname>
$ git push origin <tagname>
```

To delete a tag named `tagname`,
```bash
$ git tag -d  <tagname>
$ git push --delete origin  <tagname>
```

If authentication is prompted, make sure to generate an authentication token on GitHub and put that as the password !
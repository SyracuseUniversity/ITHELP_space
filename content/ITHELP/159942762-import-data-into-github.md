---
title: "Import Data into GitHub"
confluence_id: "159942762"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159942762/Import+Data+into+GitHub"
version: 3
last_modified: "2023-11-13T18:19:02.000Z"
status: "current"
parent_id: "159941242"
---

### Import Repositories

Code itself, including branches, and commit history can be imported using the GitHub import tool. In Gitlab create a personal access with read only abilities and when prompted give the GitHub form your username and the GitLab token. Note: does not import non-core-git things like CI/CD setup.    

<https://github.com/new/import>  

### Importing CI/CD

From Gitlab: Gitlab and GitHub use different syntax for structuring CI/CD pipelines, in GitHub called “actions ”. These are incompatible, and require the use of GitHub Action  importer to translate or be re-written.    

The  [GitHub Action Importer](https://docs.github.com/en/actions/migrating-to-github-actions/automated-migrations/migrating-from-gitlab-with-github-actions-importer#perform-a-dry-run-migration-of-a-gitlab-pipeline)    can read in CI/CD pipelines but it’s not perfect.    

The importer requires an GitHub access token with write access to the repositories you want and your Gitlab token (read access only).    

The setup can take some time but once setup it works. Unfortunately, it does not auto load secret keys values and they have to be manually created. Many of the repos use docker login to log into GitLab docker repository and build the project and to push them . This action, at least the pushing and receiving is here:  <https://github.com/docker/login-action>  and it may be worth to just rebuild the simpler ones instead of re-doing actions.

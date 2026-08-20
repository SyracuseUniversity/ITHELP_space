---
title: "GitHub Team"
confluence_id: "159942578"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159942578/GitHub+Team"
version: 11
last_modified: "2024-01-18T18:32:24.000Z"
status: "current"
parent_id: "159941242"
---

### Creating  a GitHub Team

Teams play a crucial role in managing GitHub projects and repositories. They offer the ability to regulate user access and permissions for collaborative efforts.

Consider naming your team according to the following convention:

**Department-Team(-SubTeam if needed)-Role**

Ensure that Team/SubTeam names are descriptive, and make the team "Visible" to facilitate discovery and collaboration for others.

Publicize your Team's GitHub URL within your department to encourage members to join the GitHub Team.

[Creating a Team](https://docs.github.com/en/enterprise-cloud@latest/organizations/organizing-members-into-teams/creating-a-team)

### Nesting Teams (Placing a team in a Team)

It's generally not recommended to use nested teams unless necessary.

However, establishing a hierarchy of parent/child teams can provide advantages for large teams in specific situations.

Child teams inherit the access permissions of their parent, simplifying permission management for larger groups.
Members of child teams also receive notifications when the parent team is @mentioned, streamlining communication across multiple groups.

If the current nested relationship extends access beyond the intended scope of the existing team, it's best to create another Team to represent the new scope of people.

### Team Maintainers

Establish Team Maintainers to approve requests to join the Team.

 [Setup Maintainers](https://docs.github.com/en/enterprise-cloud@latest/organizations/organizing-members-into-teams/assigning-the-team-maintainer-role-to-a-team-member)

Ensure there are at least two group maintainers. This redundancy ensures that if one person is unavailable, another Team member can fulfill the administrative duties of Team maintenance.

---

### Joining a GitHub Team

GitHub repository and project permissions are best managed with GitHub Teams. 

If you have been given a Team name to join follow these steps:

- Navigate to the [Syracuse University Organization](http://github.syr.edu)
- Select the "Teams" tab from the row of available options near the top of the page.
- Search for the Team you would like to be a member of.
- Select the Team, and click the "Request to join" button to send an access request to the Team Maintainers.

![](https://answers.atlassian.syr.edu/wiki/download/attachments/159942578/image-2023-11-7_15-0-20.png?api=v2)

A Team Maintainer will now be able to review your request to join and will approve or deny the request.

Enabling Entra ID Group Sync for GitHub Teams

GitHub Teams can be synced to Entra ID groups by following the steps at the link below.

[Synchronizing a GitHub Team with an Entra ID Group](https://docs.github.com/en/enterprise-cloud@latest/organizations/organizing-members-into-teams/synchronizing-a-team-with-an-identity-provider-group#connecting-an-idp-group-to-a-team)

Once group sync is enabled for a GitHub Team, membership can then be managed via SUPER and SU groups.

---
title: "Adding Users or Groups in Microsoft Teams"
confluence_id: "159941706"
space_key: "ITHELP"
space_name: "Information Technology Support"
source_url: "https://su-jsm.atlassian.net/wiki/spaces/ITHELP/pages/159941706/Adding+Users+or+Groups+in+Microsoft+Teams"
version: 19
last_modified: "2020-08-11T18:16:25.000Z"
status: "current"
parent_id: "159941055"
labels:
  - "teams"
  - "microsoft"
  - "class"
  - "dept"
  - "usermanagement"
---

![](https://answers.atlassian.syr.edu/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=its-toc&locale=en_US&version=2)

Microsoft Teams can use Azure AD groups to help in bulk adding members to a team.  The act of adding members to a team using the method below will **COPY** the membership of the group to the team,  it will not create a synchronized relationship between the team and the group.  Meaning if the Azure AD group membership changes, the team membership will not change.

## Adding based on a User

In Teams, click the ellipsis next to the Team name and select "Add member"

![groupAddMemberOption](https://answers.atlassian.syr.edu/wiki/download/attachments/159941706/groupAddMemberButton.png?api=v2)

On the new screen type the name, NetID or email address of the individual will be apart of the Team.  External users can be added using their email address.

![Add user to team](https://answers.atlassian.syr.edu/wiki/download/attachments/159941706/adduser.png?api=v2)

Pressing "Add" will add the selected user into the Team.

## Adding based on a Dept group

In Teams, click the ellipsis next to the Team name and select "Add member"

![groupAddMemberOption](https://answers.atlassian.syr.edu/wiki/download/attachments/159941706/groupAddMemberButton.png?api=v2)

On the new screen type the name of an AD dept group whose members will be apart of the Team.

![deptGroupAdd](https://answers.atlassian.syr.edu/wiki/download/attachments/159941706/deptAddMember.png?api=v2)

Pressing "Add" will now **COPY**all members of the dept group into the Team.

## Adding based on a Class group

In Teams, click the ellipsis next to the Team name and select "Add member"

![groupAddMemberOption](https://answers.atlassian.syr.edu/wiki/download/attachments/159941706/groupAddMemberButton.png?api=v2)

On the new screen type the name of an AD class group whose members will be apart of the Team.

![classAddGroupButton](https://answers.atlassian.syr.edu/wiki/download/attachments/159941706/groupMemberAddList.PNG?api=v2)

Pressing "Add" will now **COPY**all members of the class group into the Team.

A Class group's name is broken down as such:

Example: Class-1201-AAA-M001-Enrollment

| Piece | Description |
| --- | --- |
| Class | Signifies this is a Class group |
| 1201 | The first "1" is a Y2K fix signifying this is in the 21st century "20" means this is for the fiscal year of 2020 The last "1" means this is part one of the academic year, so the Fall |
| AAA | The unit/OU |
| 101 | Course number |
| M001 | Course Section |
| Enrollment | Signifies who the group contains. Some examples include: Enrollment, Instructor PI, and Instructor TA |

## Removing member added by Group

To remove the user from the team, they can be removed using the Microsoft Teams interface.

[Remove someone from a team](https://support.office.com/en-us/article/remove-someone-from-a-team-91610d8b-c182-4cab-8f31-1ed8d3d316ee)

## Joining a Team Using a Code

Once logged into Teams, click the Teams button on the left side of the app

Next, click Join or create a team at the bottom of your teams list.

Finally, go to Join a team with a code (the second tile), enter or paste the code in the 'Enter code' box, and click Join.

## Additional Teams How-To Pages

- [Adding Users or Groups in Microsoft Teams](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941706/Adding+Users+or+Groups+in+Microsoft+Teams)
- [Create a Team in Microsoft Teams](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941974/Create+a+Team+in+Microsoft+Teams)
- [External/Guest User Meeting Experience](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941038/External+Guest+User+Meeting+Experience)
- [External/Guest User Teams Experience](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159942021/External+Guest+User+Teams+Experience)
- [Join a Microsoft Teams Meeting](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159942184/Join+a+Microsoft+Teams+Meeting)
- [Manage Your Microsoft Teams Meeting](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159942071/Manage+Your+Microsoft+Teams+Meeting)
- [Managing Teams Notifications](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941954/Managing+Teams+Notifications)
- [Microsoft Teams Audio and Video Setup](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159942004/Microsoft+Teams+Audio+and+Video+Setup)
- [Scheduling Meetings in Microsoft Teams](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941392/Scheduling+Meetings+in+Microsoft+Teams)
- [Team and Group Expiration Policy](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159942213/Team+and+Group+Expiration+Policy)
- [Using Chat in Microsoft Teams](https://answers.atlassian.syr.edu/wiki/spaces/ITHELP/pages/159941394/Using+Chat+in+Microsoft+Teams)

![](https://answers.atlassian.syr.edu/wiki/plugins/servlet/confluence/placeholder/unknown-macro?name=toplink&locale=en_US&version=2)

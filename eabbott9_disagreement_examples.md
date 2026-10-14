# Disagreement Examples

Here are 3 different times me and my partner disagreed while I was showing them how I reviewed their projects.

## Disagreement 1

| Field | Value |
| - | - |
| Project | open-quantum-safe_ci-containers |
| Parties | eabbott9 reviewing dkim68 |
| Field | RecentThemes |
| Partner's Value | Feature development:Dependency updates |
| My Value | Features:Building |
| Winner | eabbott9 |
| Adjucated Value | Feature development:Other |
| Reasoning | The recent commits are mainly CI/build-image work plus feature changes. The partner read the second theme better, but “Building” is not in the coding guide, so I normalized it to Other. |
| Key Evidence | Recent commits add/modify CI images, remove NVCC, add GMP modules, and automate Alpine Linux image builds. |


## Disagreement 2

| Field | Value |
| - | - |
| Project | cpmech_gosl |
| Parties | eabbott9 reviewing dkim68 |
| Field | Currentstatus |
| Partner's Value | Active |
| My Value | Inactive |
| Winner | dkim68 |
| Adjucated Value | Active |
| Reasoning | The coding guide says Inactive only when the last commit is before 2025-04-01. This project has commits after that date, so Active is the correct label. |
| Key Evidence | The stats file has a last GitHub commit after the April 1, 2025 cutoff. |

## Disagreement 3

| Field | Value |
| - | - |
| Project | poissonconsulting_tmbr |
| Parties | eabbott9 reviewing dkim68 |
| Field | RecentThemes |
| Partner's Value | Documentation updates:Automated bot contributions |
| My Value | Deployment:Documentation |
| Winner | eabbott9 |
| Adjucated Value | Documentation updates:Other |
| Reasoning | The partner’s interpretation matches the actual recent messages better: several are GitHub Pages deployments and several are documentation/template updates. Deployment is not a coding-guide label, so I normalized it to Other. |
| Key Evidence | Four recent commits deploy to gh-pages and several others update/delete documentation or repository templates. |

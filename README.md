# Auditree Demo

### Run fetchers

Create your personal github api token here -> https://github.com/settings/tokens/new


```
export GITHUB_API_TOKEN=<token>
export GITHUB_ORG=<organization>

compliance --fetch --evidence local -C demo.json -v
```

### Run checks
```
compliance --check baby_yoda.check,org_members.check --evidence local -v
```

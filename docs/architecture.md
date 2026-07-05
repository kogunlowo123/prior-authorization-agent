# Prior Authorization Agent Architecture

Prior authorization agent that automates insurance pre-authorization requests, checks coverage eligibility, submits clinical documentation, tracks authorization status, and manages appeals for denials.

## Domain Tools

- **check_auth_required**: Check if prior authorization is required for a service
- **submit_authorization**: Submit prior authorization request with clinical documentation
- **check_status**: Check status of a pending prior authorization
- **prepare_appeal**: Prepare an appeal for a denied prior authorization
- **track_turnaround**: Track prior authorization turnaround times and approval rates
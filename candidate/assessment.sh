#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
compose=(docker compose -p cyberfde)
up() {
  "${compose[@]}" up -d
  for ((i=0; i<180; i++)); do
    if curl -fs -o /dev/null http://127.0.0.1:8080/login; then
      printf 'Ready: http://127.0.0.1:8080/login\nAdministrator / admin\nsales@example.invalid / assessment-demo\naccounts@example.invalid / assessment-demo\nviewer@example.invalid / assessment-demo\nportal@example.invalid / assessment-demo\n'
      return
    fi
    sleep 5
  done
  printf 'Error: login page did not become ready; inspect docker compose logs.\n' >&2
  return 1
}
case "${1:-}" in
  up) up ;;
  status) "${compose[@]}" ps -a ;;
  reset) "${compose[@]}" down --volumes --remove-orphans; up ;;
  down) "${compose[@]}" down --volumes --remove-orphans ;;
  *) printf 'Usage: %s {up|status|reset|down}\n' "$0" >&2; exit 2 ;;
esac

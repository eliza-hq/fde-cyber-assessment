FROM ghcr.io/frappe/erpnext-ci-mariadb@sha256:9f597e5f229ee27476b807c958ffa63cc5f2a303ff91e7e2b7189262521473eb
COPY --chown=ci:ci frappe /home/ci/src/frappe
COPY --chown=ci:ci erpnext /home/ci/src/erpnext
USER ci
WORKDIR /home/ci
RUN bench init --python /usr/bin/python3.14 --frappe-path /home/ci/src/frappe --frappe-branch assessment --skip-assets frappe-bench
WORKDIR /home/ci/frappe-bench
RUN bench get-app --skip-assets erpnext /home/ci/src/erpnext
RUN bench build

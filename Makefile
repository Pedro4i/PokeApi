run:
	docker compose -f compose.yaml down --remove-orphans
	docker compose -f compose.yaml stop
	docker compose -f compose.yaml build --force-rm
	docker compose -f compose.yaml up
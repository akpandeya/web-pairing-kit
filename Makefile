target: run_api run_frontend

run_api:
	pip install -r api/requirements.txt \
	&& python -m api

run_frontend:
	cd search-app \
	&& npm install \
	&& npm start dev

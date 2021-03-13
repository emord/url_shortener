prod_server:
	gunicorn shortener:app -w 4 -k uvicorn.workers.UvicornWorker

dev_server:
	uvicorn --reload shortener:app

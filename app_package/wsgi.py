from app_package.prototype import app
from app_package.prototype import write_data, scheduler

if __name__ == '__main__':
    scheduler.add_job(id='Scheduled task', func=write_data, trigger='interval', seconds=60)
    scheduler.start()
    app.run()

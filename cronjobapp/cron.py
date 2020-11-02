import cronjob



@cronjobapp.register
def periodic_task():
    print('ishwar...')


def my_cron_job():
    print('hello ishwar')
    f = open('/home/ishwar/Desktop/cronjobpro/cronjobapp/file.txt', 'w+')
    f.write('ishwar')
    f.close()

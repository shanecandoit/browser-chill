
import os
import psutil

BROWSERS = ["chromium", "firefox" , "vivaldi", "brave", "opera", "msedge", "chrome","postman"]

def chill_browsers(kill=False):

    browser_pids = []

    process_ids = psutil.pids()
    for process_id in process_ids:
        process = psutil.Process(process_id)
        # print(f"Process ID: {process_id}, Name: {process.name()}")

        for browser in BROWSERS:
            if browser in process.name():


                browser_pids.append(process_id)

                if kill:
                    try:
                        process.kill()
                    except Exception as e:
                        print(f"Error killing process: {e}")
                    continue

                print(f"Browser: {browser}, PID: {process_id}")
                print(f"Nice value: {process.nice()}")
                print(f"cpu% : {process.cpu_percent(interval=1)}")

                # affinity
                process.cpu_affinity([0, 1])
                # priority
                if psutil.WINDOWS:  # Windows (either 32-bit or 64-bit)
                    process.nice(psutil.IDLE_PRIORITY_CLASS)
                elif psutil.LINUX:  # linux
                    process.nice(psutil.IOPRIO_CLASS_IDLE)
                else:  # MAC OS X or other
                    process.nice(20)
                print(f"Nice value: {process.nice()}")



    print('chilled', browser_pids)

if __name__ == "__main__":
    # chill out the browsers
    chill_browsers()

    # kill the browsers
    # chill_browsers(kill=True)

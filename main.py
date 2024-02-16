
import os
import psutil

BROWSERS = ["chromium", "firefox" , "vivaldi", "brave",
            "opera", "msedge", "chrome","postman"]

def chill_browsers(kill=False):

    browser_pids = []

    process_ids = psutil.pids()
    for process_id in process_ids:

        try:
            process = psutil.Process(process_id)
            # print(f"Process ID: {process_id}, Name: {process.name()}")

            for browser in BROWSERS:
                if browser in process.name():
                    if kill:
                        process.kill()
                    else:
                        print(f"Browser: {browser}, PID: {process_id}")
                        print(f"  Nice before: {process.nice()}")
                        print(f"  Cpu% : {process.cpu_percent(interval=1)}")

                        # affinity
                        process.cpu_affinity([0, 1])
                        # priority
                        if psutil.WINDOWS:  # Windows (either 32-bit or 64-bit)
                            process.nice(psutil.IDLE_PRIORITY_CLASS)
                        elif psutil.LINUX:  # linux
                            process.nice(psutil.IOPRIO_CLASS_IDLE)
                        else:  # MAC OS X or other
                            process.nice(20)
                        print(f"  Nice after: {process.nice()}")

                    # it worked
                    browser_pids.append(process_id)

        except Exception as e:
            print(f"Error w process: {e}")


    print('chilled', browser_pids)

if __name__ == "__main__":
    # chill out the browsers
    chill_browsers()

    # kill the browsers
    # chill_browsers(kill=True)

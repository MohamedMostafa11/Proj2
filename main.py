from tkinter import *
from tkinter import ttk
###################################################################
root=Tk()
root.title("Process")
##################################################################
def butclick(event):
    EDF(int(entpro.get()))
def EDF(x):
    print("EARLIST DEADLINE SERVE SCHEDULLING")
    tasks = []
    n = x
    for i in range(n):
        tasks.append([])
        tasks[i].append(i + 1)
        print("Please Enter the Execution time of task:", i + 1)
        tasks[i].append(int(input()))
        print("Please Enter the Deadline time of task:", i + 1)
        tasks[i].append(int(input()))
        print("Please Enter the Arrival time of task:", i + 1)
        tasks[i].append(int(input()))

    print(tasks)
    u = 0
    for i in range(n):
        u += float(tasks[i][1] / tasks[i][2])
    print("Utilization: ", u)
    if u > 1:
        print("The tasks are not feasible")
    else:
        lcm = 1
        temp_p = []
        for i in range(n):
            temp_p.append(tasks[i][2])
        print(temp_p)
        i = 2
        while i <= max(temp_p):
            counter = 0
            for j in range(n):
                if temp_p[j] % i == 0:
                    counter = 1
                    temp_p[j] /= i
            if counter == 1:
                lcm = lcm * i
            else:
                i += 1
        print("LCM: ", lcm)
        i = 0
        instances = []
        for i in range(n):
            j = 1
            while 1:
                if j * tasks[i][2] <= lcm:
                    instances.append([tasks[i], j * tasks[i][2]])
                    j += 1
                else:
                    break
        for i in range(len(instances)):
            print(instances[i])
        for i in range(len(instances)):
            tmp = instances[i].copy()
            k = i
            while k > 0 and tmp[1] < instances[k - 1][1]:
                instances[k] = instances[k - 1].copy()
                k -= 1
            instances[k] = tmp.copy()
        print()
        for i in range(len(instances)):
            print(instances[i])
        timeLeft = []
        for i in range(n):
            if tasks[i][3] == 0:
                timeLeft.append(tasks[i][1])
            else:
                timeLeft.append(int(0))
        timeLine = []
        time = 0
        while time < lcm:
            for i in range(n):
                if time > 1 and ((time % tasks[i][2] == 0 and time > tasks[i][3]) or time == tasks[i][3]):
                    # print("true ", end='')
                    timeLeft[i] = tasks[i][1]
            anyrun = 0
            for j in range(len(instances)):
                if j == 0 and timeLeft[instances[j][0][0] - 1] > 0:
                    timeLine.append(instances[j][0][0])
                    timeLeft[instances[j][0][0] - 1] -= 1
                    anyrun = 1
                    if timeLeft[instances[j][0][0] - 1] == 0:
                        instances.pop(j)
                    # print("[",time,"]",instances[j][0][0],timeLeft[instances[j][0][0]-1], time )
                    break

                elif j > 0 and instances[j][1] == instances[0][1]:
                    if timeLeft[instances[j][0][0] - 1] > 0:
                        tmp = instances[j].copy()
                        instances[j] = instances[0].copy()
                        instances[0] = tmp.copy()
                        time -= 1
                        anyrun = 1
                        break
                elif j > 0 and timeLeft[instances[j][0][0] - 1] > 0:
                    timeLine.append(instances[j][0][0])
                    timeLeft[instances[j][0][0] - 1] -= 1
                    anyrun = 1
                    if timeLeft[instances[j][0][0] - 1] == 0:
                        instances.pop(j)
                    # print("[",time,"]",instances[j][0][0],timeLeft[instances[j][0][0]-1], time )
                    break

            if anyrun == 0:
                timeLine.append(0)

            time += 1
        print()
        mn = 0
        mx = 0
        for i in range(lcm):
            if i > 0 and timeLine[i] != timeLine[i - 1]:
                mx = i
                print(mn, "", mx, "", "[" + str(timeLine[i - 1]) + "]")
                mn = i
            if i == lcm - 1:
                mx = lcm
                print(mn, "", mx, "", "[" + str(timeLine[i]) + "]")
        print()
        for i in range(len(instances)):
            print(instances[i])
###################################################################
def butclick2(event):
    FCFS(int(entpro.get()))
def FCFS(x1):
    print("FIRST COME FIRST SERVE SCHEDULLING")
    n = x1
    d = dict()

    for i in range(n):
        key = "P" + str(i + 1)
        a = int(input("Enter arrival time of process" + str(i + 1) + ": "))
        b = int(input("Enter Executed time of process" + str(i + 1) + ": "))
        l = []
        l.append(a)
        l.append(b)
        d[key] = l

    d = sorted(d.items(), key=lambda item: item[1][0])

    ET = []
    for i in range(len(d)):
        # first process
        if (i == 0):
            ET.append(d[i][1][1])

        # get prevET + newBT
        else:
            ET.append(ET[i - 1] + d[i][1][1])

    TAT = []
    for i in range(len(d)):
        TAT.append(ET[i] - d[i][1][0])

    WT = []
    for i in range(len(d)):
        WT.append(TAT[i] - d[i][1][1])

    avg_WT = 0
    for i in WT:
        avg_WT += i
    avg_WT = (avg_WT / n)

    print("Process | Arrival | Executed | Exit | Turn Around | Wait |")
    for i in range(n):
        print("   ", d[i][0], "   |   ", d[i][1][0], " |    ", d[i][1][1], " |    ", ET[i], "  |    ", TAT[i], "  |   ",
              WT[i], "   |  ")
    print("Average Waiting Time: ", avg_WT)
###################################################################
entpro = Entry(root,width=20)
entpro.grid(column=0 ,row=0)
entpro.pack()
butEDS =Button(root,text="EDS",command=butclick)
butEDS.bind("<Button>",butclick)
butEDS.pack()
butFCFS =Button(root,text="FCFS",command=butclick2)
butFCFS.bind("<Button-1>",butclick2)
butFCFS.pack()
root.mainloop()
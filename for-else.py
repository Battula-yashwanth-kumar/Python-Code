# When we use else with for loop the complier will only gp into the else block of code when two conditions are satisified:
    #The loop is normally executed without any errors
    # we are trying to find an item that is not present inside the list or data strucuture on which we are implementing our loop


ls=["mqnckjcl","evvl[spv'sd]","qnlkksdcsdl;"]
for item in ls:
    if item=="claklskl;cla;":
        print("found")
        break
else:
    print("not found")
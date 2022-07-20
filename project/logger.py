

# =============== loggging mechanism ======================

def logger(*args, func=None, msg):
    global log_file
    if func:
        if len(args) > 1:
            output = str(func(args))
        elif len(args) == 1:
            output = str(func(args[0]))
        else:
            func()
    else:
        output = '-No output-'

    log = jdate('Y/m/d H:i:s') + '\t' + str(msg) + '\t' + \
        output + '\n' + '='*(len(msg) + len(output) + 25) + '\n'
    print(log)
    log_file.writelines(log)

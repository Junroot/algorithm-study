def convert_time(time_string):
    hour, minute, second = map(int, time_string.split(":"))
    return hour * 3600 + minute * 60 + second


def convert_format_time(time):
    hour = ("0" + str(time // 3600))[-2:]
    time %= 3600
    minute = ("0" + str(time // 60))[-2:]
    second = ("0" + str(time % 60))[-2:]
    return ":".join([hour, minute, second])


def convert_logs(logs):
    start_times = []
    end_times = []

    for log in logs:
        start, end = log.split("-")
        start = convert_time(start)
        end = convert_time(end)
        start_times.append(start)
        end_times.append(end)
    return sorted(start_times), sorted(end_times)


def solution(play_time, adv_time, logs):
    play_time = convert_time(play_time)
    adv_time = convert_time(adv_time)
    view_counts = [0 for _ in range(play_time)]
    start_times, end_times = convert_logs(logs)
    start_index = 0
    end_index = 0
    for i in range(play_time):
        while start_index < len(start_times) and start_times[start_index] == i:
            view_counts[i] += 1
            start_index += 1
        while end_index < len(end_times) and end_times[end_index] == i:
            view_counts[i] -= 1
            end_index += 1
        if i > 0:
            view_counts[i] += view_counts[i - 1]

    view_time = sum(view_counts[:adv_time])
    max_length = view_time
    answer = 0
    for current_time in range(adv_time, play_time):
        view_time -= view_counts[current_time - adv_time]
        view_time += view_counts[current_time]
        if max_length < view_time:
            answer = current_time - adv_time + 1
            max_length = view_time
    return convert_format_time(answer)

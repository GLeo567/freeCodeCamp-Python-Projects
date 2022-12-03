def add_time(start, duration, dow=None):
    # Creation of date components
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
            "Sunday"]
    am = [f"{hour} AM" for hour in range(1, 12)]
    pm = [f"{hour} PM" for hour in range(1, 12)]
    minutes = [min for min in range(60)]
    am.insert(0, "12 AM")
    pm.insert(0, "12 PM")
    one_day = am + pm

    # Component separation in paramater start
    start_list = start.split(":")
    start_hour_str = start_list[0] + " " + start_list[1][3:5]
    start_minute = int(start_list[1][:2])

    # Component separation in paramater duration
    duration_list = duration.split(":")
    duration_hour = int(duration_list[0])
    duration_minute = int(duration_list[1][:2])

    # Obtainig index of elements in start
    start_hour_index = one_day.index(start_hour_str)
    start_minute_index = minutes.index(start_minute)

    # Conversion from hours to minutes of elements in duration param
    dh_min = duration_hour * 60
    dur_min_lapse = dh_min + duration_minute

    # Calculating future hours and days:
    hours_counter = int(dur_min_lapse / 60)
    days_counter = int(dur_min_lapse / 1440)
    dc = days_counter
    # print(hours_counter, days_counter)

    # To keep iterating through lists
    dur_min_lapse = dur_min_lapse % len(minutes)
    hours_counter = hours_counter % len(one_day)
    days_counter = days_counter % len(days)

    # Index calculations for minutes and one_day lists
    min_steps = start_minute_index + dur_min_lapse

    if min_steps < len(minutes):
        nm = minutes[min_steps]
    else:
        hours_counter += 1
        j = min_steps - len(minutes)
        nm = minutes[j]

    hours_steps = start_hour_index + hours_counter

    if hours_steps < len(one_day):
        new_hour = one_day[hours_steps]
    else:
        days_counter += 1
        dc += 1
        k = hours_steps - len(one_day)
        new_hour = one_day[k]

    nh = new_hour.split()[0]
    ds = new_hour.split()[1]
    if nm < 10:
        nm = f"0{nm}"

    # If there's an element of days in parameter "args"
    if dow is not None:
        chosen_day = dow.capitalize()
        new_days_index = days.index(chosen_day) + days_counter

        if new_days_index < len(days):
            nd = days[new_days_index]
        else:
            k = new_days_index - len(days)
            nd = days[k]

        if days_counter > 1:
            new_time = f"{nh}:{nm} {ds}, {nd} ({dc} days later)"
        elif days_counter == 1:
            new_time = f"{nh}:{nm} {ds}, {nd} (next day)"
        else:
            new_time = f"{nh}:{nm} {ds}, {nd}"
    else:
        if days_counter > 1:
            new_time = f"{nh}:{nm} {ds} ({dc} days later)"
        elif days_counter == 1:
            new_time = f"{nh}:{nm} {ds} (next day)"
        else:
            new_time = f"{nh}:{nm} {ds}"

    return new_time

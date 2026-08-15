def earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration):

    res = float("inf")

    # Land 

    min_land = float("inf")

    for i in range(len(landStartTime)):
        min_land = min(min_land, landStartTime[i] + landDuration[i])

    for j in range(len(waterStartTime)):
        res = min(res, max(min_land,waterStartTime[j]) + waterDuration[j])

    # water

    min_water = float("inf")

    for i in range(len(waterStartTime)):
        min_water = min(min_water, waterStartTime[i] + waterDuration[i])

    for j in range(len(landStartTime)):
        res = min(res, max(min_water, landStartTime[j]) + landDuration[j])

    return res

    # land_set = set()
    # water_set = set()

    # for i in range(len(landStartTime)):
    #     land_set.add((landStartTime[i], landDuration[i]))

    # for j in range(len(waterStartTime)):
    #     water_set.add((waterStartTime[j], waterDuration[j]))

    # res = float("inf")

    # # Land -> Water
    # for ls, ld in land_set:
    #     land_finish = ls + ld

    #     for ws, wd in water_set:
    #         res = min(
    #             res,
    #             max(land_finish, ws) + wd
    #         )

    # # Water -> Land
    # for ws, wd in water_set:
    #     water_finish = ws + wd

    #     for ls, ld in land_set:
    #         res = min(
    #             res,
    #             max(water_finish, ls) + ld
    #         )

    # return res

landStartTime = [99]
landDuration = [59]
waterStartTime = [99,54]
waterDuration = [85,20]

def main():
    print(earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))

if __name__ == "__main__":
    main()
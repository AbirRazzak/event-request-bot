class Event:
    def __init__(self, name, desc, sdate, stime, etime, loc, estatt, estcost):
        self.name = name
        self.description = desc
        self.startDate = sdate
        self.startTime = stime
        # self.endDate is not necessary as 99/100 times it will be the same as start date
        self.endTime = etime
        self.location = loc
        self.estimatedAttendance = estatt
        self.estimatedCost = estcost

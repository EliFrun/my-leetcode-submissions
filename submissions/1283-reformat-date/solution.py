class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(' ')
        day = day[:-2]
        if len(day) == 1:
            day = '0' + day
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(month) + 1
        if month < 10:
            month = f'0{month}'
        return f'{year}-{month}-{day}'
        

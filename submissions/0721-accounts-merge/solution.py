class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_user = {}
        user_to_user = { 0: 0 }
        user_to_name = {}
        curr = 1
        def find(email):
            user_id = email_to_user.get(email, 0)
            user_ids = []
            while user_to_user[user_id] != user_id:
                user_ids.append(user_id)
                user_id = user_to_user[user_id]
            for u_id in user_ids:
                user_to_user[u_id] = user_id
            return user_id
        for name, *emails in accounts:
            ids = set()
            for email in emails:
                ids.add(find(email))
            if 0 in ids: ids.remove(0)
            if not ids:
                user_to_user[curr] = curr
                for email in emails:
                    email_to_user[email] = curr
                user_to_name[curr] = name
                curr += 1
            else:
                m = min(ids)
                for id in ids:
                    user_to_user[id] = m
                for email in emails:
                    email_to_user[email] = m

        ret_dict = defaultdict(list)
        for email, user in email_to_user.items():
            ret_dict[find(email)].append(email)

        return [[user_to_name[id]] + sorted(emails) for id, emails in ret_dict.items()]
        


            
        
        



        

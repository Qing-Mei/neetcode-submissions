from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        merge = defaultdict(list)

        for acc in accounts:
            name = acc[0]
            emails = set(acc[1:])

            unmatch = []

            for existing_emails in merge[name]:
                if emails & existing_emails:
                    emails.update(existing_emails)
                else:
                    unmatch.append(existing_emails)
            
            unmatch.append(emails)
            merge[name] = unmatch
        
        res = []

        for name, email_group in merge.items():
            for emails in email_group:
                res.append([name] + sorted(emails))
        
        return res

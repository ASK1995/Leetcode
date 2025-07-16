class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            uniques.add(local + '@' + domain)
        return len(uniques)
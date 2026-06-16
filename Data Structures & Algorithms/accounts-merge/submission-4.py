class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
    def find(self, i):
        # check if parent is the same as i
        if self.parents[i] == i:
            return i
        # Path Compression: Update the parent pointer to the root
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, i, j):
        email_i = self.find(i)
        email_j = self.find(j)

        # Check if they have same parent
        if email_i != email_j:
            self.parents[email_i] = email_j
            return True
        return False

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        n = len(accounts)
        dsu = DSU(n)
        email_to_idx = {}
        for i, account in enumerate(accounts): # i is the account index
            for email in account[1:]:          # skip the name at index 0
                if email in email_to_idx:
                    dsu.union(email_to_idx[email], i)
                else:
                    email_to_idx[email] = i

        mergedGroup = defaultdict(set)
        for email, index in email_to_idx.items():
            # we need to find "ultimate captine" for this email account
            root = dsu.find(index)

            # add the merged email to the captains group
            mergedGroup[root].add(email)

        results = []
        for root, email_set in mergedGroup.items():
            name = accounts[root][0]

            # sort
            sorted_emails = sorted(list(email_set))

            results.append(([name] + sorted_emails))
        return results

class Solution:
    
    def reverseList(self, head):
        if not head or not head.next:
            return head
        
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    
    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        if k == 1:
            return head
        
        li= []
        
        follower = None
        sub_head = head
        runner = sub_head
        counter = 0
        while runner:
            
            follower = runner
            runner = runner.next
            counter += 1
            if counter == k:
                follower.next = None # cut of the list
                node = self.reverseList(sub_head)
                li.append(node)
                counter = 0
                sub_head = runner
                follower = None
        
        if follower:
            li.append(sub_head)
        
        for i, node in enumerate(li):
            temp = node
            while temp.next:
                temp = temp.next
            if (i+1) < len(li): 
                temp.next = li[i+1]
        print(len(li)) 
        result = li[0]
        return result

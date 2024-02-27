class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    results = []
    to_visit = [self.root]
    while len(to_visit) > 0:
      node = to_visit.pop()
      if node['id'] == id:
        return node
      else:
        to_visit = node['children'] + to_visit
        results.append(node)
    
    return None


  
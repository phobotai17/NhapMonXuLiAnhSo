#2374802010148_truonghieuhoai
from collections import defaultdict

# Import NetworkX để vẽ đồ thị
import networkx as nx

# Import matplotlib để hiển thị đồ thị
import matplotlib.pyplot as plt

# Khai báo class đồ thị
class Graph:
    def __init__(self):
        # Khởi tạo một dictionary mặc định dạng danh sách kề
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        # Thêm cạnh từ đỉnh u đến v (đồ thị vô hướng nên cần thêm cả hai chiều)
        self.graph[u].append(v)
        self.graph[v].append(u)  # Thêm cạnh ngược lại để đảm bảo đồ thị vô hướng
        
    # Hàm đệ quy để thực hiện DFS từ đỉnh v
    def DFSUtil(self, v, visited):
        visited[v] = True  # Đánh dấu đỉnh v đã được thăm
        print(v, end=' ')  # In ra đỉnh hiện tại
        
        # Duyệt qua các đỉnh kề chưa được thăm
        for i in self.graph[v]:
            if not visited[i]:  # Nếu đỉnh chưa được thăm
                self.DFSUtil(i, visited)  # Gọi đệ quy DFS cho đỉnh chưa thăm
                
    def DFS(self, v):
        # Tạo danh sách visited với số phần tử bằng số đỉnh lớn nhất + 1
        visited = [False] * (max(self.graph) + 1)
        # Bắt đầu DFS từ đỉnh v
        self.DFSUtil(v, visited)

# Chạy chương trình
if __name__ == "__main__":
    g = Graph()  # Tạo đối tượng đồ thị
    
    # Thêm các cạnh (đồ thị vô hướng nên thêm cả hai chiều cho mỗi cạnh)
    g.addEdge(0, 1)  
    g.addEdge(0, 2)
    g.addEdge(0, 3) 
    g.addEdge(1, 4) 
    g.addEdge(1, 5)  
    g.addEdge(4, 6) 
    g.addEdge(5, 7) 

    # In kết quả DFS từ đỉnh 0
    print("DFS - duyệt tìm kiếm theo chiều sâu bắt đầu từ đỉnh 0:")
    g.DFS(0)

    # Vẽ đồ thị bằng thư viện networkx
    G = nx.Graph()  # Đồ thị vô hướng
    for u in g.graph:
        for v in g.graph[u]:
            G.add_edge(u, v)  # Thêm cạnh vào đồ thị

    pos = nx.spring_layout(G)  # Bố trí vị trí các đỉnh

    # Vẽ đồ thị:
    # - with_labels=True: hiển thị tên các đỉnh
    # - node_color: màu đỉnh
    # - edge_color: màu cạnh
    # - node_size: kích thước đỉnh
    # - font_size: cỡ chữ
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            edge_color='gray', node_size=700, font_size=16)

     # Hiển thị tiêu đề và đồ thị
    plt.title("Đồ thị minh họa DFS từ đỉnh 0")
    plt.show()
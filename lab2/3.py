# Import defaultdict để tạo dictionary với giá trị mặc định là list
from collections import defaultdict

# Import thư viện NetworkX để xây dựng và vẽ đồ thị
import networkx as nx

# Import matplotlib để hiển thị hình ảnh đồ thị
import matplotlib.pyplot as plt

# Khai báo lớp Graph để tạo và thao tác với đồ thị
class Graph:
    def __init__(self):
        # Sử dụng defaultdict để lưu danh sách kề
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        # Thêm cạnh từ đỉnh u đến v (vì là đồ thị vô hướng nên cần thêm cả hai chiều)
        self.graph[u].append(v)
        
    # Hàm đệ quy hỗ trợ cho thuật toán DFS
    def DFSUtil(self, v, visited):
        visited[v] = True           # Đánh dấu đỉnh v là đã thăm
        print(v, end=' ')           # In đỉnh v ra màn hình

        # Duyệt qua tất cả các đỉnh kề của v
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)  # Gọi đệ quy tiếp tục DFS với đỉnh chưa thăm
                
    def DFS(self, v):
        # Khởi tạo mảng visited với kích thước đủ lớn, đánh dấu tất cả các đỉnh là chưa thăm
        visited = [False] * (max(self.graph) + 1)
        
        # Bắt đầu DFS từ đỉnh v
        self.DFSUtil(v, visited)

# Chạy chương trình chính
if __name__ == "__main__":
    g = Graph()  # Tạo một đối tượng đồ thị

    # Thêm các cạnh vào đồ thị (thêm hai chiều vì là đồ thị vô hướng)
    g.addEdge(0, 1)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 4)
    g.addEdge(4, 2)
    g.addEdge(1, 4)
    g.addEdge(4, 1)
    g.addEdge(1, 3)
    g.addEdge(3, 1)
    g.addEdge(3, 4)
    g.addEdge(4, 3)
    g.addEdge(3, 5)
    g.addEdge(5, 3)
    g.addEdge(5, 4)
    g.addEdge(4, 5)

    # In ra màn hình thứ tự duyệt DFS bắt đầu từ đỉnh 0
    print("DFS - duyệt tìm kiếm theo chiều sâu bắt đầu từ đỉnh 0")
    g.DFS(0)

    # --- VẼ ĐỒ THỊ ---
    
    # Tạo đồ thị vô hướng bằng NetworkX
    G = nx.Graph()
    
    # Thêm các cạnh vào NetworkX từ danh sách kề của đồ thị g
    for u in g.graph:
        for v in g.graph[u]:
            G.add_edge(u, v)

    # Xác định vị trí hiển thị các đỉnh bằng spring layout (bố cục lò xo)
    pos = nx.spring_layout(G)

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
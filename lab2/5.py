from collections import deque  # Nhập khẩu deque, một cấu trúc dữ liệu hàng đợi hai đầu, nhưng không được sử dụng trực tiếp trong triển khai A* này.
import networkx as nx  # Nhập thư viện networkx để vẽ đồ thị
import matplotlib.pyplot as plt  # Nhập thư viện matplotlib để hiển thị đồ thị

class Graph:
    def __init__(self, adjac_lis):
        # Khởi tạo đối tượng Graph.
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        # Trả về danh sách các hàng xóm của một đỉnh v cùng với trọng số cạnh.
        return self.adjac_lis.get(v, [])

    def h(self, n, h_values):
        # Hàm heuristic (ước lượng) cho đỉnh n.
        return h_values.get(n, float('inf'))

    def a_star_algorithm(self, start, stop, h_values):
        # Triển khai thuật toán tìm kiếm A*.
        open_lst = set([start])  # Tập hợp các đỉnh cần được đánh giá.
        closed_lst = set([])  # Tập hợp các đỉnh đã được đánh giá.

        g_score = {start: 0}  # Chi phí từ đỉnh bắt đầu đến chính nó là 0.
        came_from = {start: start}  # Đỉnh bắt đầu không có đỉnh nào đi trước nó.

        while len(open_lst) > 0:
            n = None
            # Tìm đỉnh n trong open_lst có f_score (g_score + h_score) thấp nhất.
            for v in open_lst:
                if n is None or (g_score.get(v, float('inf')) + self.h(v, h_values)) < \
                               (g_score.get(n, float('inf')) + self.h(n, h_values)):
                    n = v

            if n is None:
                print('Đường đi không tồn tại!')
                return None

            if n == stop:
                # Nếu đỉnh hiện tại n là đỉnh đích, tái tạo và trả về đường đi.
                reconst_path = []
                while came_from[n] != n:  # Đi ngược từ đích về đến đỉnh bắt đầu.
                    reconst_path.append(n)
                    n = came_from[n]
                reconst_path.append(start)  # Thêm đỉnh bắt đầu vào đường đi.
                reconst_path.reverse()  # Đảo ngược đường đi để có thứ tự đúng từ bắt đầu đến đích.
                print(f'Đường đi được tìm thấy: {reconst_path}')
                return reconst_path

            # Duyệt qua tất cả các hàng xóm (m) của đỉnh n.
            for (m, weight) in self.get_neighbors(n):
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)  # Thêm m vào open_lst.
                    came_from[m] = n  # Đặt n làm đỉnh liền trước của m.
                    g_score[m] = g_score[n] + weight  # Cập nhật g_score của m.
                else:
                    if g_score.get(m, float('inf')) > g_score[n] + weight:
                        g_score[m] = g_score[n] + weight  # Cập nhật g_score của m.
                        came_from[m] = n  # Cập nhật đỉnh liền trước của m.
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            open_lst.remove(n)  # Xóa n khỏi open_lst vì nó đã được mở rộng hoàn toàn.
            closed_lst.add(n)  # Thêm n vào closed_lst.

        print('Đường đi không tồn tại!')
        return None

if __name__ == '__main__':
    # Định nghĩa danh sách kề của đồ thị.
    adjac_lis = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('D', 10), ('E', 12)],
        'C': [('A', 2), ('E', 7)],
        'D': [('B', 10), ('E', 6), ('Z', 15)],
        'E': [('B', 12), ('C', 7), ('D', 6), ('Z', 9)],
        'Z': [('D', 15), ('E', 9)]
    }

    # Định nghĩa các giá trị heuristic cho mỗi đỉnh.
    h_values = {
        'A': 1,
        'B': 1,
        'C': 1,
        'D': 1,
        'E': 1,
        'Z': 1
    }

    graph = Graph(adjac_lis)

    # Định nghĩa đỉnh bắt đầu và đỉnh kết thúc.
    start_node = 'A'  # Thay thế bằng đỉnh bắt đầu bạn muốn
    stop_node = 'Z'   # Thay thế bằng đỉnh kết thúc bạn muốn

    # Gọi thuật toán A* để tìm đường đi.
    path = graph.a_star_algorithm(start_node, stop_node, h_values)

    # Vẽ đồ thị bằng thư viện networkx
    G = nx.Graph()  # Đồ thị vô hướng
    for u in graph.adjac_lis:  # Duyệt qua từng đỉnh trong danh sách kề
        for v, weight in graph.get_neighbors(u):  # Duyệt qua từng hàng xóm
            G.add_edge(u, v, weight=weight)  # Thêm cạnh vào đồ thị

    pos = nx.spring_layout(G)  # Bố trí vị trí các đỉnh

    # Vẽ đồ thị
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            edge_color='gray', node_size=700, font_size=16)

    # Nếu có đường đi, vẽ đường đi
    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]  # Tạo danh sách các cạnh của đường đi
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)  # Vẽ đường đi

    plt.title("Đồ thị minh họa A*")  # Đặt tiêu đề cho đồ thị
    plt.show()  # Hiển thị hình vẽ
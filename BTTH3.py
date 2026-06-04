
available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0
MAX_CAPACITY = 50

def calculate_ticket_cost(quantity: int, seat_class: int) -> float:

    if seat_class == 1:
        unit_price = BASE_PRICE
        class_name = "Economy"
    elif seat_class == 2:
        unit_price = BASE_PRICE * 1.5
        class_name = "Business"
    else:
        return -1.0  # invalid class

    subtotal = unit_price * quantity
    service_fee = subtotal * 0.05
    total = subtotal + service_fee
    print(f"\n-> Xác nhận đặt chỗ:")
    print(f"   Số lượng: {quantity} | Hạng: {class_name}")
    print(f"   Tạm tính: ${subtotal:.1f}")
    print(f"   Phí dịch vụ (5%): ${service_fee:.1f}")
    print(f"   Tổng thanh toán: ${total:.1f}")

    return total
def process_booking(quantity: int, total_cost: float) -> None:

    global available_seats, flight_revenue

    if quantity > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
        return

    available_seats -= quantity
    flight_revenue += total_cost
    print(f"\n✅ Đặt vé thành công! Ghế trống còn lại: {available_seats}")
def process_refund(quantity: int) -> float:

    if available_seats + quantity > MAX_CAPACITY:
        print(f" Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra.")
        return -1.0

    refund_amount = BASE_PRICE * 0.8 * quantity
    available_seats += quantity
    flight_revenue -= refund_amount

    return refund_amount

def print_flight_status() -> None:
 
    booked = MAX_CAPACITY - available_seats
    print("--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"   Sức chứa tối đa       : {MAX_CAPACITY}")
    print(f"   Ghế đã đặt            : {booked}")
    print(f"   Ghế trống             : {available_seats}")
    print(f"   Tổng doanh thu hiện tại: ${flight_revenue:.1f}")


def get_positive_int(prompt: str) -> int:
    """Nhắc người dùng nhập số nguyên dương, lặp cho đến khi hợp lệ."""
    while True:
        raw = input(prompt).strip()
        if raw.lstrip("-").isdigit():
            value = int(raw)
            if value > 0:
                return value
        print("   ⚠  Vui lòng nhập số nguyên dương hợp lệ.")

def main() -> None:
    """Vòng lặp chính của hệ thống SkyBooking."""
    while True:
        print("\n============= SKYBOOKING SYSTEM =============")
        print(" Chuyến bay: VN2026 | Khởi hành: Hà Nội")
        print(" 1. Đặt vé máy bay")
        print(" 2. Hủy vé & Hoàn tiền")
        print(" 3. Xem tình trạng chuyến bay")
        print(" 4. Đóng hệ thống")
        print("=============================================")
        choice = input("Chọn chức năng (1-4): ")

        match choice:
            case "1":
                print("\n--- ĐẶT VÉ MÁY BAY ---")

                qty = get_positive_int("Nhập số lượng vé: ")

                while True:
                    raw_class = input("Chọn hạng vé (1: Economy, 2: Business): ").strip()
                    if raw_class in ("1", "2"):
                        seat_class = int(raw_class)
                        break
                    print("   ⚠  Hạng vé chỉ gồm 1 (Economy) hoặc 2 (Business).")
                total = calculate_ticket_cost(qty, seat_class)
                process_booking(qty, total)

            case "2":
                print("--- HỦY VÉ & HOÀN TIỀN ---")
                qty = get_positive_int("Nhập số lượng vé muốn hủy: ")
                refunded = process_refund(qty)
                if refunded >= 0:
                    print(f"Hủy vé thành công. Hệ thống đã hoàn lại: ${refunded:.1f} (80% giá cơ bản).")
                    print(f"   Ghế trống hiện tại: {available_seats}")
            case "3":
                print_flight_status()
            case "4":
                print(" Cảm ơn đã sử dụng SkyBooking. Phiên làm việc kết thúc.")
                break
            case _:
                print("⚠  Vui lòng chọn từ 1 đến 4.")
    main()
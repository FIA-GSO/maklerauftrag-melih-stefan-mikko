def calculate_area_of_segment(lengths, widths):
    areas = []
    for i in range(len(lengths)):
        area = lengths[i] * widths[i]
        areas.append(area)
    return sum(areas)

def main():
    print("Willkommen im Raumrechner!")
    num_rooms = int(input("Gebe die Nummer der Räume ein: "))
    
    rooms = {}
    
    for room_num in range(1, num_rooms + 1):
        room_name = input(f"Gibt den Namen des Raumes ein: {room_num}: ")
        num_segments = int(input(f"Gibt die Menge der Segmente an {room_name}: "))
        
        segment_lengths = []
        segment_widths = []
        
        for i in range(num_segments):
            segment_lengths.append(float(input(f"Gib die Länge des Segment an {i + 1} in {room_name} (in Meter): ")))
            segment_widths.append(float(input(f"Gib die Weite des Segments an {i + 1} in {room_name} (in Meter): ")))
        
        total_area = calculate_area_of_segment(segment_lengths, segment_widths)
        rooms[room_name] = total_area
        
        print(f"\nDie Gesamtfläche des Raums {room_name} is: {total_area} Quadratmeter")
    
    print("\nRaum Flächen:")
    for room, area in rooms.items():
        print(f"{room}: {area} Quadratmeter")

if __name__ == "__main__":
    main()

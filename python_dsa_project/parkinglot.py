class Parking_lot:
    def __init__(self):
        self.capacity = 0
        self.no_of_ocpd_slot = 0

    def create_parking_space(self, capacity):
        self.parking_slots = ['-1' for _ in range(capacity)]
        self.capacity = capacity
        return self.capacity

    def get_empty_slot(self):
        for slot_id in range(self.capacity):
            if self.parking_slots[slot_id] == '-1':
                return slot_id
            else:
                continue

    def parking_of_vehicle(self, reg_no, colour):
        if self.no_of_ocpd_slot < self.capacity:
            slot_id = self.get_empty_slot()
            self.parking_slots[slot_id] = reg_no+"  "+colour
            self.no_of_ocpd_slot += 1
            return slot_id+1
        else:
            return -1

    def leave_parking(self, slotid):
        if slotid > self.capacity:
            return -1
        elif self.no_of_ocpd_slot > 0 and self.parking_slots[slotid-1] != '-1':
            self.parking_slots[slotid-1] = '-1'
            self.no_of_ocpd_slot -= 1
            return True
        else:
            return False

    def get_slot_no_by_registration_no(self, registration_no):
        for slot_no in range(self.capacity):
            if registration_no in self.parking_slots[slot_no]:
                return slot_no+1
            else:
                continue
        return -1

    def show_all_parked_cars(self):
        print("Slot No. Registration No. Colour")
        for i in range(len(self.parking_slots)):
            if self.parking_slots[i] != '-1':
                print("   "+str(i+1)+"\t   "+str(self.parking_slots[i]))
            else:
                continue

    def get_slot_no_of_all_car_by_colour(self, colour):
        list_of_slotno = []
        for slot_no in range(self.capacity):
            if colour in self.parking_slots[slot_no]:
                list_of_slotno.append(str(slot_no+1))
        return list_of_slotno

    def get_regno_of_all_car_by_colour(self, colour):
        lst_of_regno = []
        for i in range(self.capacity):
            if colour in self.parking_slots[i]:
                temp = self.parking_slots[i]
                lst_of_regno.append(temp[:(len(temp)-len(colour)-1)])
        return lst_of_regno

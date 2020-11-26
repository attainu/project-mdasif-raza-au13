from parkinglot import Parking_lot
import argparse


class Parking_Commands(Parking_lot):
    def show(self, line):
        if line.startswith("create_parking_lot"):
            num = int(line.split(' ')[1])
            res = self.create_parking_space(num)
            print('Created a parking lot with '+str(res)+' slots')

        elif line.startswith('park'):
            reg_no = line.split(' ')[1]
            colour = line.split(' ')[2]
            res = self.parking_of_vehicle(reg_no, colour)
            if res == -1:
                print("Sorry, parking lot is full")
            else:
                print('Allocated slot number: '+str(res))

        elif line.startswith('leave'):
            leave_slot_id = int(line.split(' ')[1])
            status = self.leave_parking(leave_slot_id)
            if status == -1:
                print('Slot number '+str(leave_slot_id)+' is not available')
            elif status:
                print('Slot number '+str(leave_slot_id)+' is free')
            else:
                print('Slot number '+str(leave_slot_id)+' is already free')

        elif line.startswith('status'):
            self.show_all_parked_cars()

        elif line.startswith('registration_numbers_for_cars_with_colour'):
            colour = line.split(' ')[1]
            regnos = self.get_regno_of_all_car_by_colour(colour)
            print(', '.join(regnos))

        elif line.startswith('slot_numbers_for_cars_with_colour'):
            colour = line.split(' ')[1]
            slotnos = self.get_slot_no_of_all_car_by_colour(colour)
            print(', '.join(slotnos))

        elif line.startswith('slot_number_for_registration_number'):
            reg_no = line.split(' ')[1]
            slotno = self.get_slot_no_by_registration_no(reg_no)
            if slotno == -1:
                print("Not found")
            else:
                print(slotno)

        elif line.startswith('exit'):
            print("Thank You!! For Using Our Parking Lot")
            exit(0)

    def main(self):
        parkinglot = Parking_Commands()
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', dest='srcfile', help="Input")
        args = parser.parse_args()

        if args.srcfile:
            with open(args.srcfile) as f:
                for line in f:
                    line = line.rstrip('\n')
                    parkinglot.show(line)
        else:
            while True:
                line = input("$ ")
                parkinglot.show(line)


if __name__ == '__main__':
    run_parking = Parking_Commands()
    print("Welcome To Our Parking Lot")
    run_parking.main()

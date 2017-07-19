#!/usr/bin/python
# -*- coding: utf-8 -*-


class Record(object):
    def __init__(self, timestamp, uuid, value, description):
        self._timestamp = timestamp
        self._uuid = uuid
        self._value = value
        self._description = description

    def timestamp(self):
        return self._timestamp

    def uuid(self):
        return self._uuid

    def value(self):
        return self._value

    def description(self):
        return self._description

    @classmethod
    def parse(cls, csv_row):
        timestamp = float(csv_row[0])
        uuid = str(csv_row[1]).lower()
        value = float(csv_row[2])
        description = str(csv_row[3])
        return Record(timestamp, uuid, value, description)

    def is_activity(self):
        return self.uuid() in [
            # Initial list
            "7e9cac8b-cca2-4396-b325-23edc21fde3a",  # "Toilet"
            "5d98492f-f954-4419-a59f-d53d9fd44ef9",  # "Leaving home"
            "7ba1ee75-a15f-467a-8bdc-9cb49efdef77",  # "Dinner"
            "4174d1ab-cbe7-44e8-a72e-4d6b04ae7eb7",  # "Entered home"
            "3db877ff-bd74-4ddc-a3ec-939c57b364a3",  # "Washing hands"
            "6242f8db-b666-4f50-8b64-05435d601aa7",  # "Preparing to sleep"
            "ba0f9491-dea3-4059-b4ad-7bd08cabe1aa",  # "Cooking dinner"
            "65865b45-765b-4038-9e92-d9a5c358fba9",  # "Breakfast"
            "7c5d5f96-4667-4d35-9bf1-4cf604e2bc35",  # "Watching TV"
            "f3ea9886-d956-4a7a-b9c4-95edaba56e13",  # "Cooking breakfast"
            "c1678225-c5cf-4399-ad48-0703dc718a86",  # "Shower"
            # Added for Max
            "95eddaf9-69be-41bc-9eaf-6a4e524ba48e",  # "Washing dishes"
            "889f3ef1-4c37-4f79-b19b-e78e512b82dd",  # "Music"
            "def2c8f2-a7ea-47a4-a58a-a5544e917023",  # "Rest with computer"
            "7c5d5f96-4667-4d35-9bf1-4cf604e2bc35",  # "Working with computer"
        ]

    def is_sensor_data(self):
        return self.uuid() in [
            "bc3c94b6-9c70-4e2c-9205-0b5d3476c7d6",  # "MI_SCALE"
            "EBEFD083-70A2-47C8-9837-E7B5634DF528".lower(),  # "KitchenBeacon4"
            "d9114d7c-6168-4471-805e-95c5ed325dc5",  # "Heart Rate Sensor"
            "3ec3d2ca-4624-4943-a2f6-69e222c57393",  # "Apple TV"
            "EBEFD083-70A2-47C8-9837-E7B5634DF525".lower(),  # "BedroomBeacon1"
            "EBEFD083-70A2-47C8-9837-E7B5634DF524".lower(),  # "KitchenBeacon0"
            "EBEFD083-70A2-47C8-9837-E7B5634DF527".lower(),  # "BathroomBeacon3"
            "EBEFD083-70A2-47C8-9837-E7B5634DF526".lower(),  # "ToiletBeacon2"
        ]

    def is_device_state(self):
        return self.uuid() in [
            # Initial list
            "0489ee1d-8919-42ce-a130-14aa0562f48b",  # "Bedroom TV",
            "a9a2eefe-f409-45b2-92ee-d5e5cd3d29c2",  # "Bathroom Shower"
            "c2bc678c-ed73-45c6-8804-bcaf645f0891",  # "Kitchen Light"
            "42c46854-3ddd-4896-b271-c051e4edacb8",  # "Toilet Light"
            "66ca0cbc-6d48-4264-be78-8914412f27ed",  # "Bathroom Light"
            "ed646245-3030-4251-8320-14e228fed987",  # "Bedroom Light"
            "0b6889f4-b87c-46c5-98c9-b8c3263cd8eb",  # "Kitchen Kettle"
            "dcdb6cef-f9b3-461e-81b2-54ad37736ef4",  # "Kitchen Water"
            "12421fda-3bfd-4eda-8534-ca7f5ba8bf8f",  # "Hall Light"
            "1d145529-a34b-4b9c-94dc-df1021589cd9",  # "Bathroom Water"
            # Added for Max
            "35cf38bf-693e-412b-89ac-88a5998f66c0",  # "Computer"
            "4faee1a1-d3d7-48c7-a097-42bcdd87e9a9",  # "Kitchen Cooker"
            "1b0ada96-f4e0-4edc-8441-d0ed12d9ba53",  # "Kitchen Local Light"
            "9660cb58-ab9f-448b-add8-ed5d76e3de66",  # "Bedroom Local Light"
        ]

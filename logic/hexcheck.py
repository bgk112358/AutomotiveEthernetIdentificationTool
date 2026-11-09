import string


def check_hex_numbers(min_did, max_did, view=None):
    numbers_are_correct = True
    if min_did.startswith("0x"):
        min_did = min_did[2:]
    if not all(c in string.hexdigits for c in min_did):
        if view != None:
            view.show_info_message("Not a hex number", "You need to write minimal logical address in hex number")
        numbers_are_correct = False
    if len(min_did) > 4:
        if view != None:
            view.show_info_message("Hex number too long", "You need to write number between 0x0000 and 0xffff")
        numbers_are_correct = False
    if max_did.startswith("0x"):
        max_did = max_did[2:]
    if not all(c in string.hexdigits for c in max_did):
        if view != None:
            view.show_info_message("Not a hex number", "You need to write minimal logical address in hex number")
        numbers_are_correct = False
    if len(max_did) > 4:
        if view != None:
            view.show_info_message("Hex number too long", "You need to write number between 0x0000 and 0xffff")
        numbers_are_correct = False
    if numbers_are_correct:
        if len(min_did) == 0:
            min_did = 0x0000
        else:
            hex_s = min_did
            a = int(hex_s, 16)
            min_did = a
        if len(max_did) == 0:
            max_did = 0xffff
        else:
            hex_s = max_did
            a = int(hex_s, 16)
            max_did = a
        return min_did, max_did
    return None, None

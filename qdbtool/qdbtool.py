import argparse
import zlib 
import sys
import uuid

def parse_args():
    parser = argparse.ArgumentParser(
        prog='QDBTool',
        description='Parse Qshrink4 database files',
    )
    parser.add_argument('infile')
    parser.add_argument('outfile')
    return parser.parse_args()

def parse_qdb(filename):
    with open(filename, 'rb') as f:
        bs = f.read()
    
    if bs[:4] != b"\x7fQDB":
        print("[-] Invalid QDB header")
        sys.exit(-1)
    
    guid = bs[4:20]
    print("[+] header GUID: ", uuid.UUID(bytes=guid))
    return zlib.decompress(bs[0x40:])


def main():
    args = parse_args()
    print("[+] parsing ", args.infile)
    contents  = parse_qdb(args.infile)
    print("[+] Writing output to ", args.outfile)
    with open(args.outfile, 'wb') as f:
        f.write(contents)
    


if __name__ == "__main__":
    main()
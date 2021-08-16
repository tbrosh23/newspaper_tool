phrase = 'M Ps|tomorrow|.|Mr.|Michael|Foot|has'
archive = []
exists = False
for i in phrase:
    exists = False
    for j in archive:
        if i == j:
            exists = True
    
    if not exists:
        archive.append(i)


print('Total num in the archive: %d\n', len(archive))
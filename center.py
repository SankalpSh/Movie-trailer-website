import media
import fresh_tomatoes
logan = media.Movie("Logan",
                  "It shows the child of wolverine created using his DNA",
                  "https://www.foxmovies.com/s3/dev-temp/en-US/__58ee7b057ede7-d7cf04fac544f21211765fde26a2d48c83276ac5-7ef2d0101093dfff.jpg",  # noqa
                  "https://www.youtube.com/watch?v=Div0iP65aZo")
a_beautiful_mind = media.Movie("A Beautiful Mind",
                             "An extraordinary mathematician who won an oscar for his work",  # noqa
                             "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMSEhUTEhIVFhUXFxcWFhgVFRgXFxUYFRcWFxcVFxgYHSggGBolHRUVITEhJSkrLi4uGB8zODMtNygtLisBCgoKDg0OGxAQGisdHR0tLS0tLS0rLS0tKy0tLS0tLS0tKy0tLS0tLSstLSsrLS0tLS0tLS0tLS0tLS03Ny03Lf/AABEIARIAuAMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAFAAIDBAYBBwj/xABBEAABAwIEAwYDBgQEBgMBAAABAgMRAAQFEiExQVFhBhMicYGRMqGxFCNCUsHwBzNy0RVikuFDU4KisvEkRHMW/8QAGgEAAwEBAQEAAAAAAAAAAAAAAQIDBAAFBv/EACURAAICAgICAwEAAwEAAAAAAAABAhEDIRIxBEETUWEiQnGBI//aAAwDAQACEQMRAD8A8oNtVciiV0ISaGk0WBCrhpUjQCdArsVwV2uCIVK0qN9fpUNOSa44K2SFKIPzOw8k1obLbck+Q9tNayVs5rqfSY+laPDwoxlJE8qhkRpwsOtpOhJ04eKCDzEn9RtRhK1KbgjxCCDsT76H6GhDLqWxK1HTVQOU7dCmZ8quWN3brH3TgM/hk6TyknKdtvasxsB67z75SVCEqA0GmU7KAnrXBYOcNRuNeFUMbfyuJI0UgkE7ZkzstPBYPHiK0GH3AcbzIgKTuBtHGKaSoz5Y8l+ohQ08BEVGWn+Rog2+envU6bnyoaMWyiyHuRpzqH1fhok1da8I86JWtyk8qaMEwWY1yxe4pNRm0e/LW3uCDyqBKa746DyMm1YP8qIps3+R961DSBpU61CKPx2DkZlpp4CI/wB65R7KedKu+Nncjw/E3RAA5zQynqM0ytj2E7XKVKuOOiu1yuiuOFFLLXa7XHFizb1FaexdgayY00AJMcIkAVkkE8DRuwv1aZwSOcT9KlkTaL4ZUwzdla1BQb20+KQB0gan9zRPDrAOwS0Qr86CM0wdDMmNetVrNKFiQrJ1Cgkj0VINEGrfLqh9K+YUIPumQazN+jco+wP2vZWnKFiQPCkkhSkkbAx04iPKq3Zy9KFAGYOx/Q86tdpbrvEQttKHEcQZJA4HpyNVMBbCj57zt69etU/wI1/6Be+uShREDgfQ8qrIxIz8Iqt23uFMONADRSJ16UHs8QKzsfnU/jdWZMiqTRsLe+J/BRC2cUdk0CsNefzo9aN+dKkrJMKNZjwq0hmorW386It2qf2avGhCEIipkkVcas2+IqyhpocBVuLOBwbmlRMlrpSruDOs+XyabNImuAVQodpUoroFccKug10JqZm1KuFAKi30RBNPyUQZsCaJs4cAB1pHNIvDx5SADbCjw/SillbqTBI18v1FaCwwtJ3A9q0Nhh6BHgHPnUJ5zTHxFHbZQwfCnF6hBG0mCfrWwt8MWloiSk8Y3+W1W7JEAaae00WtG5SdoMT/AHmpxXIOTJx0eSdocLyrIVsdJ4ec0zA8OUhaeRPhI4K/KfOtl2yw1SRmiUiZ6UIwpxPcOJJBSRPVKhqNRtpXNtaHVSSkgb25Qhzu5GqZSRtE8I4UCsrRI2qx2hvO9WlUycoCupGgV7VHZa8KdRbR5+d/2w5ZpHM0TacSONDrZrSYNZ3tViJbOVGYfKgsZBM3f2qONSt4lHE/Osf2JxRToUlQJI41q0IHKu4tM5sJNYh5+1TG6nhVe3QOVWAnpV4p0TbGlU8KVTtiuU/FnWfPEUq6a5TljtPQmuCpm00GFKya2Zk0atWRA8qoWqKLsJ2qM2b8EEStM1aQPpUbO+/yqdSZ8+XCs7NqCFgiSPmOVHLRragVloNd6N4esRvMfWpSOl0HWF6CjFgvbrpWftTrx96OWIH0OtVxMwZ1olxRgLbIOx+VeW4g0q2K4EoWCnbdQ1Ar1i4HhisN2nblQbAmSlXEfCZ9fSny92Dxpao8yxRIQoJUVTGYgaRn1ynyqXDXkcSr3ol2j7N3KWV3xyqbzgLj4k5zAO0KTmI220oHh6zy+VUq4mTNfN2axi8bA1UR5ms92hu2FzCwTwqriijQA77UYQ9iG/7EXtshBGcBR4VubdIUJTBFeO4RfBJAIE+Qr1HstiqVACdfKqRjslMPsMnlVruTyqZp5POnvXVV4pIRFZKNdfpSqtdXlKpudDUz54NcmnEVyKcuOTVhg1WFTtqoMaL2FLU0atoIrOsO0Zs3Dp++FQmj0MEkFksDfWmEwRVi3cEQeXHWqVwCAKzmwuNuk7Hh5TRzCBJjXy2rOWjoB12ozb4wy3usTSyi/oDkqNbaoEgUZt9B8qwlh2nazDxA9K1eF44y5pmimhrsxZotrWw06JEceFZHtBYKNw0nU5woE7QEkEn2+la9vKRpqOfCgHa55TPdvIykpzJIImAuAT8qtNWrIeO3z4oz3bO5W3LIV/8AHTZrcSkCApQHxK5kFI96wtjfcYHtWm7bYohdihStFLcLWn5BDyh5SEiKxti83zIrorQnldpVtdncWvCdNKzjqtTWivw2ojxH2oNcsthWiz7VWLM6KqFQRFbns06UrT4o05VkbVpsqEqPtWns0pB0JNdJnM9JZuBp4hUzl2OYrFIuo/NUisQ6n5Uk8jrQkVs1pfB/9Vyss3ifU+4pVhk52alGNHl5FJQg1wqpKVXqkxU4Ipk10GuOJxbkayPepWblSdlTFVm08j7T6invxMj25RQGTa2g6xihUAAdf3pWnbsS8gZRsNev9q8/sT4x51612Le8OXckQNKy5lXR6GDLKUW2Y7E7cN+FSiDyTQN8tzuqtt2yw78YA5K0g+/Ks5ZgJBBEhQieIniKaElWzssHLoisLZhW5VAIBJCoTJ0kgaeteidmsCYIC0kERMhWYemtZrsvaKD4cGiswUIzAFQEBRB003jaYrdPYBbtgFpsJUEgEp0zHmRxNTyO/Z0biqaqw1hjgjw7D9PrQnt00taWUISVFSlJ6zEx8qIYNbZU/vhVh9gF9lw/CgL/ANRiD56U0bcDOmo5eR5L2/t+5atWlEFQLq1AcD4UwayVooTqK9O7ZdlvtD+YKOVKQE+aiVqPqVUKtuwX+Y/KqxVKjJlycptsyjpTE5TQm5W2T8J969Kf7DKjQ/SsdjHZC6Qo5Wsw6EU0UxFJAixLWcZkmPOtXZqanQGPesza4Q9nhTah7Vt8IsFgSUn1pZhbRxV42Pw1SdvEE/CfSj7jB4J+lCnmyFfAan0KiJotkfCaVTByB8JpUbj9FNnnJaNNUKk72mKVOta3VHISaeGyajBqZtVIPGvZIlEU1xNTJNQvK1rikkkiSy0UK9Q7ACXk9BXmFoNRNeo/w3T95pUMvaNOB1jkbW+wdLhOnpwrzvFsE7lZhMoJ0/y9D0r0/Gb3uE51DQDUj2rMv3KHs3SfUVHJSeh/FlNq30BMKdS3qBr+xWosnSo67a+kUFZwwE6ab/PWjtpblB1/enEVFW2XytUG7dED9+tVr7E0NqCVRMT/AG+lT26iRP6e1eb9rsS/+Y6kfhKUeyQfqTW/HFPs8bLJx2jZIWhWpVqdd9qstMI5/OvO7a/86K218dNTW6ME1pmFzfs3JbajU/OhOJotT8S/+6grt0SN6z2L5jsaGl2MnyDaba2zGD86KsMtBOhrz+wS5m3rSpcUABSPg+jncS3fd2nXMB5mglw4gnRQqHFXVnSNKBF5ys0ysGFX3QPxUqBreXSqDiaEZWkk0jXE1rFO09JqOnCuGTLQXpUEydaeNqjIoIaTLtsoEjzr0z+HtyEOAHjz+leTtrg16H2IZUt0DkMx1ioZvs2eM1JNHrXaG1D1u+gkT3SynbQhJUPmK8iwTEj4dd4+YE1ssTFyQ4FuwFgpyIAgJO8KOpJHHrWHfsFtL/tUZyUjR40HCNXaPQ8KIJkcpHlRhY0zbdOlZTs7dkFPoI/tWuQNPOlxrRLyFUiw2rTXbjHTjXl9013rrjhSDmWpXuTHyit32gvgzbOL4kBCRP4nDGnkCTWJtHdBWzG0eV5F3SOtWkcBU6QBvA89OE/oamDo6U1awd/P5EfQ/OtMZpLTMji32WGlJI/DuBPn+u3vTXrVJ3Kf9XIlJEcYKVD0qMKSBlG0zvxBBn5CpG1IkGNjI1OhkSf+0eevOhKVjRVDW7ZtJMqSCN9RpIJ+gJ9KupbQRoZ1jfiNx51E8pC95139ApI+Sle9ObWEiATElXPUmT9TU+bj0M42V7q2SdwaCXdqBtR9xc8TVN9BPE+1Z8mSTHhFIzD7HSlRd9hX5j7Uqj8jNKR5WTTZrpriRNbxDs10Gk5vTQaBxKFU6ajSaSSa46y9hrGdYTWt7J35RdKGw29IGnzrHWTiwoFG9Hra4X3gWlASs9RE6VHImz0PGriem4heJ6kDQx0qi2tDohW+p21HKhOHqunoBQ3EQVSoBPCZ4noKpYlbvoWQh0xoD4QOH+1Y+LNqSXRoMOHiVlIJRqQN+da+2fkQd9PWsd2OKu+Vm101nnFa9gCdOPyoxVEfIZU7R4YX0Np0gKKtSRsIG2+pNDGOzRH5fdVa1aUKOQmFJTm3/DOWfenf4d1Pv861Qin0ePlTszCuzyiCMyQSCAZOhqIdlXP+cPM5tNQoaeQIPSKPPWzgURkOUGAoSfDoJKdyZO3EQRsRUD9k54fAZKQVCVEBU+JMg8BBn8UxVEvwnQLb7ILgAvJMZdysfDmmdeMj261N/wDyB0i5jwgcTJAOpE/vQ1YRhrhJzII8BO51VyCp2MDXrVdzDFx4QSYB1CkyTOYandMD+qRR/wCHUTq7LjMT9o8OWI+igeczPpVc9mgIm8nnwmUxz4Ekg9BXHcNVrCCRm8OitU5VkTroZSlPTMaT+EwSA3mEGNSJVkkA8hmgZuVBq/QCb/BWwAC/JA11Gvv1mmHCm/8AnfMVGjDkymW4GYA6EkApJzb6AGE+c8Iq1/h7Q2oKBxF/g7f/ADPpSpxaSNjSpuMPo65Hz0alth4h71FU1odT5U5UY8Naiqy+mq8UDjoroNNFOTRCW7V4ijdjdapOUDjQazaBrR4U02TlUD6GoZKN/jcl7NjhOLjLHqeWo1j/AGp76O8VMTJjz0O1UUYSEIzJOxAg7EHiOQitFgVmAJP9/WsbVm2TS2dw+3Sy3njxHTqY/WiuGczvx6UNurkKUEjYfD+qjRLDTG+3En3mmj2QyW439lNq6nF+63T9nQ2R/WlxR/SreEYoWT3S5UiSEmZIjQjXaI2rOdhnjc4nc3X4O8UEf0tp7sH9atYoUi4eb4lWdPQqAOnzozbh/S+zK0paf0blu6bVqlQPkf2a6FAkDqB89PrXmF9iamocBITMLI3QeCvKimG9roUG341AKVDiDsfOr4/J5dozzwNdGoTjTKhICvhK4gHZGcDTQk6gDmDyprmLNbgFQkxBGY5Rm2VBE6ATvIpyLgKEpII6RTSvmPkKup2QarsacUbJOVKjEayBM96djsful6HXYVZzJMEcRPuOPWoC9J29YE1xdxSuaBR10DlVC5dj8NWXLkULvrmozzJdBSK9xekbJFKht05SqXzMNHjdOYMGm0knWt4xbd1qopNTFVNOtccR5aUUfsMJ79vT4hoOWuwPQnT2qsmw3BEEaEEagjeR8qXmiixNlfC4nX/3VzDbsh2Dz+dQnD429wassWImTM+f9qWTVF4Kaqj0PDbxK0gHYATr86ncxQAZUnfcideg/vWStlQAJ086ttvczWRwN6/TR2LkwRz3471T7Xdoe6aLTRlxfhGXfXShV5jIaQYImn9g8FVdPpuXpyyS2Og3WR7Aetco1/TJ5Zo3H8O8DNpZJz/zFiVdCTJE+dZf+IF13V6hQMZmkqMc0qUn+1emvEBIGwA0HLlXi/8AFW8BvEJ3ysCehUtR+laHDSTPOU3bZYXfhUgahQnXYmNqCuJlPdZtCczKidUH8Tfv9aFtYiQR+/Kp7h4ZsswlwZh/lVx8uFIsfEpztF7Ae17turKokjYidq9KwztAi4TKVa8udeI385pMZtj161bwXFFNKHiIFGePVxJ6emeyu4iQYMg8jUa8SoBhHaZK/A8Arz3rSNWbK4yn0mvPySnHsLxfRAbwmoVvzV5eFgcDVd2yA4KrNLMDhQPdVrXasG0HJVKgsx3E8RNdFdIrgFfREh811umipEQN65sJr+yKgCMwBSRlUOYPCtBj+Bd8O9ZBLqACvh3yODn9Y2P/AKrFW90LdIUsSsgKQiSInZTkapB4J3PSo2O1l4l1LwfOZMgCB3eUkEoyDTLoOvWs/CTlaNCyJILotFkfy1/6T/anG0c4Nr/0Ko/g2OpvApTYyPAZlspPxAfE41zHTcVx7FiNjPrUXOSdUaVkVWgCq3eA/lL9Ux9TVd0OgGQBH5lAVZxPGCZk1nypTqtSQniarC2rYs83pBDDcNVcuAE5kzGxyk8deQ1J8q9l7KWwSjMBAgJSOSU7H1kn1rIYBhaUpTlGigB5I0k66gq+lbu2WEoAHKpc+WT8RPI6h+sffXGUTXgPbK8Ll64s9EjySK9kxy78JrxXtCzDqlczNXhK5sg41ArWFqt5xDTYBWtWVIJA1gkSTtsaJ3OC3ASMyBotaR40kEoZD69eKe7IM7GY3qxhLTdo1bXygtxxTy+7QkhCUJYOVRKik5lkq0GgitElwPWC7kZhAu3A5lSSHGUNW6VKAGqnW3YUrbMjNAJqxNMzGI4I9kKlICVNobLkqGiXQS3P+Y5SRwjiTFVLzs5cM5u8SkZFobVC0mFrnKnTqDJ4da3SG8t25YEqDqLfuAtKiW9Gi8tnu1SS0QSApSiUkApAFPxPDlvG4yFBS87bXDQUlcrZWG1Kukqz+Hu/tCARGXwnTQ0EFnn9y2pC1oUIcaWptYBkAoJSQCN9QduVHMF7SqSQFHSpcdt7dxj7ckQq4evI+9CAQh1vKsNrBLilB0lQBEcABpWUUCDypJ41JUykZM9fwvtLoBPCtExiLa+nWvEbLEFAjX0NaiwxeACTyrzc3jV0XVSPS1rRzFKss1ioW3mBBjX2rlY3iD8aPHSKaBTzTa+jMR1Iq9hzA8bqhKGgDH51kw2jynU9BVEVoLNofZkCPjK3FdYVlT7RNLJ0NFWwC5JJWTJJJJ6mmRVpxvIopO371qFaYNFCs7bPLbWlbailaSClQ3BrUYpjbdwlDwAQ6rR5GwzASHEc0njWTqRHWhKCl2MpNF+4ifvFEA6wBJjymambxhLYhlhOb873iI6pRsPM1Xw7Dy+4202PG4tCAOqiASegEqJ2gGr3aLAVWtw6wTKUK8C9u8SoBSViN5SRtpoaHFew8n6IsE7TP27ve5i4FGXEqPxydSD+FXKNOFevYdi7b7KXWlSlXuDxSocCK8twXs8w7aXN0868gW5bzJbS2rMHFBIIKjOnLpWi7LYKbbEHrT7QooLH2kFKBlWgICwFJJlDgChsf0pJ409o6M/sNYs/PGsH2htpk1r3rxh5tDtutS0kHMFAAoOhCSEk6+dQ9psDLJYDhMOoQSU5TlUVZXEcpTKTrzqEFKMi7acTBWOMutILQyKbKs+R1CXEBY/GkHUHTh6ip7XH7kFsIWBkU6pICRBFwR3yVCIUhWUAg6CBtFT9rcEbs7122C1rS0pIUohAUcyErOUDoob1fucGsre5Wyq5uu9S8G05G2ohaG4WonTUuKEDgmthlGoN8qUkIzBHc5xkDndQB3feb5YKRprHGqqbh8AIUtST3Krds8mlZ0qbH5knOr36CtDiduzb3blr9tui+l5pvVtkIWXFNpJBGohK5/6aluOzbarq7acuXstm266VBDRKu6SlbkJ4TIjypHY8WYn/ABZ4Mi2OTInvIBQCpHekZ8qtxJSkT0FVRqOZH61sMM7O2d84otP3ACbdx5coakKaI8OhI1SZketAOzNk0+t0LU4kIt3n0lGUkhlGfKrMdJA3HGmO6BrO9Ebx3KlI6bjcdav3eDNIsba9StwqfccbyKCMqO6KgTI1MxQW+XO9I1seL0aDs7dEpcSTplP0rtD+zTxCiP8AKr6GlWTJD+i8HaANMmniuEVvMQgaM2F1KEpP4QU+hOYfWgtWLNcKHWlkrQ0XTCl+zmEihMcOVGwZFDbxuDMUsH6HnH2UjXUHWksU0VUkbLspbhph+8dbWpASbdrKoIKl3AKXFoWpJylLecTB1VFGu0CBeWVteMtq+7m0eTm7xSQiC0sqCUyIMTA+IV59aOnaTHKTHTTatFYsFTQUDAzRpIngfPUD2qc5UhoqzQ9k2X0YdiJYbKnAWMgCM5UULlUJI8cCTAmjmD2ubEG3g2E3LmHvG6QnVKH1BCUAiSEqUI8HDSsy5hwc0EhQCSDJ4gVocH7OoVhaB/8AZaW9dBMnMWluFpXmCGwfNIpY5E0NPHT/ANgHCGb/AL5p67tu6ZYbddcCWktl1DADmQpG5K8qAd4Wd4opZYs3iVk+ltpaX7Zz7WG1OF1ZC1kvoEtp4pJyxuelVsCwNt29bddMMtqbW5JMKUtaUMNafmcUn0BrOY7aqt8Ye7takFN2CkglJha0LI04eM+9PGpKxXadBbt7gT11iLj9uhTjFz3a23kDM2EhttCs69kRlMgkVnsbeFxiy1M+NK7lrIU65ghTacw6eFVbH+Jziv8AGm0BSsoNp4cxCfE7qco0M/pUfb3so1dd9fYaPE24tN3bp0W2pCiFOoSk8R4iBuDI4imFYH7YMKPaBfhUc90wpGh8aQWiVJ5gZVSRyNa9tK04jjCkjxdxc5AUghRU02WyArRU69DWHwLE3v8ACcSSHlhKVWWUZz4A64sLCTOgUEgEDQgda1PZnEXh2fcWh1xLibsNpWFqzpSS34UqJlI1286DQYgvsN2h768KH1NIU5avW6SlKWhnV4k5kjZR1EnlQjBsFeshdOXbS2EptLm3BcEd4882GkIb/PJUTI0AB1o5g3aha30W2IhN3bOqS3982lS2lOHKFocgKnMQDJ6giNQf8SMC+yXS2gVKSgjIVEn7tYlB14jxJJ45ZoJ6Gad0F04O+9guHpaaWtSX7lSgkSoJUVhKsu8E1h8WYU04tpeikKKVCZgjdMjQxtpxFRWzsHc+5/vTbqJ0o+zlpFvBF/eDmQR8qVRYQuHkHqPnSqM42ysJaKgFJYrtPirkUQ11Jj0pGuVwA5brkA027RpVfDHt0+tWLlWlSqmXvQJNMp6jTTVUZ2PaP7mtFhGJAMlszmQZ1OhSTunyms60df3yq2ngRw0pZq0NB0bBm8IdHLKg+yQf9q3Ruza3Vo4QQEW7bbgiAUOlS1exIP8A01gbB9KsigYVkQeRBSAJHUFNFm7pRgLUtX9SlK/8iaxt8TTXIMdskotVIZZVKUvpuVnlCgplvfUJRJ9RQL+KdmpOMJUEqh77KtGh8RzhCo6yEz5jnSxLUfvht9KyuI3rwIh9/TUffu6HaR4tDHKr4p8kSnGjbfxJZJx1rQyo2kQDrDhOnPY1n8Qx64w7Fbl1k6h9YWhQIS6krzBKv9Ug8PeRT9+9APfv7CPv3dPLxaelC7x9bklxa1nYFa1LMcpUTpVkybR6J2oFk5hd3e2UoFy7aB1mB9y624tStBtOfy4jendlLZauzz2VClRe54ShSiUpU1mIA1IGuo5GvLA4QFAKUEqjMASArKZTmGxg7TtR3s/fqAIN0+gpLaUBNytvKhSjnKRmGgEnQcdq5vQF2H8L7POuvtrUhTbLbiHHXXUqbbbQ2sKPiWACTAEDXXpVTtnjyb++fcEhpeVpud8jeiVkb6qJV5ECrmIq70HvX3XAELP3j6noWlXgylajqR4tOdDTh9slZzPDKFuaZx8IVDagQNTAMjhIqaaqivuzL5cqik7iQafcVob6wtiEOFckpSFhLqPjzIEJnQkpzkGYJHCKD3SU+MJOYBSgCJhQBIChOsEc9aYUrYf/ADEf1ClTbc+JPmPrSoMaPREKkj/amAVKoacdP7U5NBlnBGFJQTckKUkEiWhlmNNeR5022wVhSZNwoETIzNxIURAnXaDRm27zuEpShkAoSkFSyDOUgKjIdda47bOLWVFljwlKUeIy2QrOozk5qAnpXCgqwwlmEKNzlJBzSpvQgxA+tW38NZ278mUkiFNcIkdNDNWb3EnEqSnuAS6FQkKEgJnTxJATv+9K59peLZSbQ5oKSczfJQBjlqPahQUwWvA2e8KftMDLIJU34jmgjlEER6004LbyR9pOmX8bf4kknhwIiiFi0pie5sVJKgkH79tWaIMQqY9KaMSLYZCrcNp+AKW4jL8ASFKKQSIiduNMApu4IwlOb7UNuKm4mRvGvHhypycLRnCVPojKTKSkRwSPESKKPMXAeS4hTCUHJmSCohQSpbhhZa0BTO3SrDVu5KB3bRLYUn4zCi5kUT/L1EHSgziO2wptSAUPFRbzJlJQZ0zTAHWpkHIJU6g/DtoTJjid+NKzLix32RAlaSBKsxDasp/4egVGnrRdB7wZgEgnqeE6aioTW9loy0QuIQpPxjnuKzmK2Df3f3mqlBJGZIyiCo+sCjl2pY8KkJOh1zbE6CSoDiKatxa9kJGVQnMowdNhlSZ3FdBUdJgZzDmYQO/J4Tmb8zVR7DGAsJ78woxmluBKSQTpprl96LpaWWkgobgKSfiVEIXI/BO4j1p7jyyonu0fdgq1WdQSRpCOaD71VCMziMIt51uCNFmczf4VEAARrIg0rTCmMrazcaqCSRnbBEpKjwkQQRRu7LiEurKG95JzkkEagAZNRA+VJbyye+HcrSkL1QtagZCZg93GkH1NEUs2tq3lAC82wV4kbEHUwOEVWusKZkguRqOKBoQDOo6/Kr9n3mo8InVJSVKgSBqCgTrUly4Z07skKVoVnNoCNsu/Go+y12gHb4c0tsIU7qsZj4m/CoagDTQ7b0CU2lLrjYJKQpSQZBmOo035VsghxGWUNkBChuokiU5j8G+lZTH2yi4Ur8xnpmEbfI+9OmKDmhCwOopVYebMpWBEx5TSo2HZAN6nySOPtUBVrVlt3T3phEEbLEWCkJcStBSEwpLr3jIBnwpMJ1G8fi6VYRiFqdyrgf5t1mVqSQSFRyTMcqziqaRRFaL95dtLcTLai2kqkLdW5nBiCM+qdpirDb9lwtdxxKiOH5lTwPXU8NKEUprji7iK2FBCWmUoOc5iAdUmIGsnnxoy3ZWq1EJZbO+gDogDeSCDy48KzK64rXck+ZNEBslW0pjIozsM7+g22K4gCaSyhJjVKpB+N4kyAABrHGsZkHKrCVaRJ56EwaBwdwdT2UIUy4UqDkOZ3ZgBQSkJCsui+MTrRezdCCMrbwQAQSUORPhgyTw8VYhMAgwNCOHXf98qnvLcBZUANTM/OaVpMdHoF4nMkKS2pR1kHMmQRvv1mq/d6fynZkE5c/IcjrqPlWcwfEfwq4n386v3jQIkVKuLoerQy+WlOXKl1KfiIJWgqE6QVE8+HXnQx66BcJl4IIAgOSvQcVKkETJjrTGUAKWAIlJ/Q1E5VQUNVeeMZlOqRBCklyCZB4jQCnsLBKAhRbZB8aFvnXWVQCRoRVR6oCKYRmysrlgKELTsEk96SSY1gZuetErpDeQyUhUAZknxdTqdz+tefsKhQPWtwlUtA6HQczymoZdFcaKi3Ed3GZYIVIVmBWqYGT4oAETtrNB7r7xtQzElJzJzaqMDUEjjH0oo6SoaASP7/Oh8ZVk8N/fh0oRYziUmF+CDw196VJxGUqT6jyO3yrlUqxCiamZ2NKlTsmiE02uUqJx2lSpVwBHhSpUqIDoqRGxpUqAUNXx8v0ohc8PIfQUqVAZFTiK0jB8A8qVKpzHiDf8Aieh+lVF0qVOcyu9UNcpUxNiOx8q2tt/LT/SPoKVKo5ukVxkDJ1H740OuNvT9a7SpIlGVL3dH/wCY/wDJVKlSq8eiMuz/2Q==",  # noqa
                             "https://www.youtube.com/watch?v=aS_d0Ayjw4o")
deadpool = media.Movie("Deadpool",
                     "A mutant that is very funny and awesome",
                     "https://m.media-amazon.com/images/M/MV5BYzE5MjY1ZDgtMTkyNC00MTMyLThhMjAtZGI5OTE1NzFlZGJjXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
                     "https://www.youtube.com/watch?v=gtTfd6tISfw")
cars = media.Movie("Cars",
                 "This is the story of a car Lightning Mcqueen",
                 "data:image/jpeg;base64,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",  # noqa
                 "https://www.youtube.com/watch?v=SbXIj2T-_uk")
rocky = media.Movie("Rocky(1976)",
                  "This is the story of an Underdogg Boxder",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoEKeON71v32FdsRwsWurlT3ncjyixUgTN8mweBnFr9rEgqWln",  # noqa
                  "https://www.youtube.com/watch?v=7RYpJAUMo2M")
coco = media.Movie("Coco",
                 "This is the story to revive the great grandfather soul in after-world",  # noqa
                 "http://t3.gstatic.com/images?q=tbn:ANd9GcS3FGIsangc2iauB89mttkiBAvIDj_O952Ypk2p5QqABby--L6d",  # noqa
                 "https://www.youtube.com/watch?v=zNCz4mQzfEI")
movies = [logan, a_beautiful_mind, deadpool, cars, rocky, coco]
#creates an array of movies
fresh_tomatoes.open_movies_page(movies)
#this calls fresh_tomatoes sends all the information from module movies

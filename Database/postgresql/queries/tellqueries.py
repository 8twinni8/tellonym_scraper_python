INSERT_TELL = """INSERT INTO public.tell
                (
                    "id", "tell", "answer", "createdAt", "parent", "sender", "receiver", "media"
                )
                VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s
                );"""
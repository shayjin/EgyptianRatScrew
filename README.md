# Egyptian Rat Screw (ERS)
[What is ERS?](https://bicyclecards.com/how-to-play/egyptian-rat-screw/)

## Tools:
- Python (PyGame)
- Git
- Visual Studio Code
## Contributors
- Jay Shin (shin.810@osu.edu)
- Ella Lee (Artwork) (lee.10086@osu.edu)


## Demo

<img width="694" alt="ers" src="https://user-images.githubusercontent.com/83435667/179071314-c9513084-7440-45b1-9ae8-8e4a00deb752.png">


## Cases Considered

방어 (플레이어 1 전에 있는 현제 살아있는 플레이어가 플레이어 1을 공격한 케이스):
방어하는 내 차례에서 슬랩해야할떄가 아니면 카드를 냄
낸 카드가 마지막 카드였는데 일반 카드일때 -> 바로 죽음
낸 카드가 마지막 카드였는데 어택 카드일때 -> 바로 죽진않고 다음 플레이어가 방어 성공하면 죽음. 방어 실패하면 테이블에 있는 모든 카드를 얻음
낸 카드가 마지막 카드였는데 슬랩이 형성될때 (찬스 남아있던 안 남아있던)-> 일반적으로 진행... should_slap() 함수 호출 
낸 카드가 마지막 카드가 아니고 일반 카드일때 ->  방어 실패 방어 실패, 코드가 계속 실행되고 player1_defense() 함수를 계속해서 부름
낸 카드가 마지막 카드가 아니고 어택 카드일때 -> 방어 성공, 다음플레이어로 넘어감
낸 카드가 마지막 카드가 아니고 슬랩이 형성되지 않지만 찬스가 남아있을때 -> 방어 실패, 코드가 계속 실행되고 player1_defense() 함수를 계속해서 부름
낸 카드가 마지막 카드가 아니고 슬랩이 형성되지 않지만 찬스가 남아있지 않을때 -> 라운드 패배
슬랩 미스인데 카드가 남아있을때 -> 그냥 slap_at_wrong_time() 함수 호출
방어하는 내 차례에서 슬랩 미스로 카드를 다 잃었을때 -> 게임 패배, 다음 플레이어 차례로 넘어감

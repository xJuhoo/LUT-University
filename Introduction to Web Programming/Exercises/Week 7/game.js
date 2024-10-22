// Juho Rekonen
// Student number: 441410

// All images are either from https://phaser.io/ example game or linked below :
/* Fireball: https://www.cleanpng.com/png-fireball-fire-planet-with-swirling-flames-spinning-8058311/
Heart: https://pngtree.com/freepng/red-3d-heart-emoji-realistic-shadow_7581933.html
Coin: https://pngtree.com/freepng/golden-dollar-coin-money_5505816.html
Skeleton: https://www.cleanpng.com/png-death-halloween-clip-art-take-the-skull-of-the-cru-411255/
*/

/*I modified the teachers example by having an hp counter that goes down if the player is hit by a bomb or touches a skeleton, and goes up if the player shoots a fireball to a skeleton. Other than that I did some  changes to how the platforms are created and tried to fix few things that annoyed me such as the player disappearing when jumping "out of bounds" (i.e., outside the game width) */
let game

const gameOptions = {
    playerGravity: 820,
    playerSpeed: 300
}

window.onload = function() {
    let config = {
        type: Phaser.AUTO,
        backgroundColor: "#117711",
        scale: {
            mode: Phaser.Scale.FIT,
            autoCenter: Phaser.Scale.CENTER_BOTH,
            width: 800,
            height: 1000,
        },
        pixelArt: true,
        physics: {
            default: "arcade",
            arcade: {
                gravity: {
                    y: 0
                }
            }
        },
        scene: new PlayGame()
    }

    game = new Phaser.Game(config);
    window.focus();
}

class PlayGame extends Phaser.Scene {

    // Let's make the player have an hp and instead of collecting stars the player collects coins. He also has the ability to destroy skeletons with fireballs
    constructor() {
        super("PlayGame")
        this.score = 0;
        this.hearts = 3;
    }
    preload() {
        this.load.image('sky', 'assets/sky.png');
        this.load.image("coin", "assets/coin.png");
        this.load.image('fireball', 'assets/fireball.png');
        this.load.image("heart", "assets/heart.png");
        this.load.image("ground", "assets/ground.png")
        this.load.image('bomb', 'assets/bomb.png')
        this.load.spritesheet("player", "assets/player.png", {frameWidth: 32, frameHeight: 48})
        this.load.image("skeleton", "assets/skeleton.png");
    }

    create() {
        // Reset score and hearts
        this.score = 0;
        this.hearts = 3;
        this.platforms = this.physics.add.group({
            immovable: true,
            allowGravity: false
        })

        this.add.image(400, 300, 'sky'); // Background from Phaser.io
        this.add.image(770, 30, "heart").setScale(0.02)
        this.add.image(25, 25, "coin").setScale(0.02)
        this.heartsText = this.add.text(725, 15, this.hearts, { fontSize: '30px', fill: '#ffffff' });

        // Player
        this.player = this.physics.add.sprite(game.config.width / 2, game.config.height / 2, "player")
        this.player.body.gravity.y = gameOptions.playerGravity
        this.physics.add.collider(this.player, this.platforms)

        // Make the player always start from a platform (and not from a free fall to death most likely)
        let startPlatform = this.platforms.create(game.config.width / 2, game.config.height / 2 + 50, "ground");
        startPlatform.setVelocityY(gameOptions.playerSpeed / 6);

        // Coins
        this.coins = this.physics.add.group({})
        this.physics.add.collider(this.coins, this.platforms)
        this.physics.add.overlap(this.player, this.coins, this.collectCoins, null, this)

        // Enemies
        this.skeletons = this.physics.add.group({})
        this.physics.add.collider(this.skeletons, this.platforms)
        this.physics.add.overlap(this.player, this.skeletons, this.attack, null, this)

        // Bombs
        this.bombs = this.physics.add.group({});
        this.physics.add.collider(this.bombs, this.platforms);
        this.physics.add.collider(this.player, this.bombs, this.hitBomb, null, this);

        // Fireballs
        this.fireballs = this.physics.add.group({})
        this.physics.add.collider(this.fireballs, this.skeletons, this.hitSkeleton, null, this)

        this.scoreText = this.add.text(45, 12, "0", {fontSize: "30px", fill: "#ffffff"})
        this.cursors = this.input.keyboard.createCursorKeys()

        // Animations
        this.anims.create({
            key: "left",
            frames: this.anims.generateFrameNumbers("player", {start: 0, end: 3}),
            frameRate: 10,
            repeat: -1
        })

        this.anims.create({
            key: "turn",
            frames: [{key: "player", frame: 4}],
            frameRate: 10,
        })

        this.anims.create({
            key: "right",
            frames: this.anims.generateFrameNumbers("player", {start: 5, end: 9}),
            frameRate: 10,
            repeat: -1
        })

        this.triggerTimer = this.time.addEvent({
            callback: this.addPlatform,
            callbackScope: this,
            delay: 500,
            loop: true
        })
    }

    addPlatform() {
        /* While creating platforms I want to make sure that the platforms cannot be spawned inside each other and that the height differences between your current platform and the next lowest platform is possible to jump. getChildren() gets all platforms currently on the screen and we reduce these platforms down to single value, in this case the lowest Y position (=highest platform)*/
        let lastPlatformY = this.platforms.getChildren().reduce((minY, platform) => {
            return Math.min(minY, platform.y);
        }, game.config.height);

        let newY = lastPlatformY - Phaser.Math.Between(100, 180);

        if (newY > 0) {
            let newPlatform = this.platforms.create(Phaser.Math.Between(0, game.config.width), newY, "ground");
            newPlatform.setVelocityY(gameOptions.playerSpeed / 6);

            // To make sure that only a coin or a skeleton spawns into a platform
            let hasCoin = Phaser.Math.Between(0, 2);

            if (hasCoin) {
                let coin = this.coins.create(newPlatform.x, newPlatform.y - 40, "coin");
                coin.setScale(0.02);
                this.coins.setVelocityY(gameOptions.playerSpeed / 6);
            }

            if (!hasCoin && Phaser.Math.Between(0, 1) === 0) {
                let skeleton = this.skeletons.create(newPlatform.x, newPlatform.y - 40, "skeleton");
                skeleton.setScale(0.08);
                this.skeletons.setVelocityY(gameOptions.playerSpeed / 6);
            }
        }
    }
    hitBomb(player, bomb) {
        this.hearts -= 1;
        this.heartsText.setText(this.hearts);
        if (this.hearts <= 0) {
            this.heartsText.setText(this.hearts)
            this.add.text(game.config.width / 2 - 100, game.config.height / 2, "Game Over", { fontSize: '80px', fill: '#fff' });
            this.scene.pause();
        }
    }   

    collectCoins(player, coin) {
        coin.disableBody(true, true);
        this.score += 1;
        this.scoreText.setText(this.score);

        if (this.score >= 15) {
            this.add.text(game.config.width / 2 - 100, game.config.height / 2, "You Win!", { fontSize: '80px', fill: '#fff' });
            this.scene.pause();
        }

        var x = (player.x < 400) ? Phaser.Math.Between(400, 800) : Phaser.Math.Between(0, 400);

        var bomb = this.bombs.create(x, 16, 'bomb');
        bomb.setBounce(1);
        bomb.setCollideWorldBounds(true);
        bomb.setVelocity(gameOptions.playerSpeed / 2);
    }

    attack(player, skeleton) {
        skeleton.disableBody(true, true);
        this.hearts -= 1;
        this.heartsText.setText(this.hearts);
        if (this.hearts <= 0) {
            this.heartsText.setText(this.hearts)
            this.add.text(game.config.width / 2 - 100, game.config.height / 2, "Game Over", { fontSize: '80px', fill: '#fff' });
            this.scene.pause();
        }
    }

    shootFireball() {
        // Create a fireball at players current position
        let fireball = this.fireballs.create(this.player.x, this.player.y, "fireball").setScale(0.005)

        // Set velocity depending on the direction the player is facing
        if (this.facing === "left") {
            fireball.body.velocity.x = -400; // Adjust speed as needed
        }
        else if (this.facing === "right") {
            fireball.body.velocity.x = 400; // Adjust speed as needed
        }
        else {
            fireball.destroy()
        }
    }

    hitSkeleton(fireball, skeleton) {
        fireball.destroy(); // Destroy the fireball
        skeleton.destroy(); // Destroy the skeleton
        this.hearts += 1;
        this.heartsText.setText(this.hearts);
    }

    update() {
        if (this.cursors.left.isDown) {
            this.player.body.velocity.x = -gameOptions.playerSpeed;
            this.player.anims.play("left", true);
            this.facing = "left"
        }
        else if (this.cursors.right.isDown) {
            this.player.body.velocity.x = gameOptions.playerSpeed;
            this.player.anims.play("right", true);
            this.facing = "right"
        }
        else {
            this.player.body.velocity.x = 0;
            this.player.anims.play("turn", true);
        }

        if (this.cursors.up.isDown && this.player.body.touching.down) {
            this.player.body.velocity.y = -gameOptions.playerGravity / 1.6;
        }

        // Fire a fireball when spacebar is pressed
        if (Phaser.Input.Keyboard.JustDown(this.cursors.space)) {
            this.shootFireball();
        }

        // Out of bounds effect where we "teleport" the player to the other side
        if (this.player.x < 0) {
            this.player.x = game.config.width;
        }
        else if (this.player.x > game.config.width) {
            this.player.x = 0;
        }

        if (this.player.y > game.config.height + 50 || this.player.y < 0) {
            this.scene.restart();
        }

        // Remove fireballs that go out of bounds
        this.fireballs.getChildren().forEach(fireball => {
            if (fireball.x < 0 || fireball.x > game.config.width) {
                fireball.destroy(); // Remove fireball if out of bounds
            }
        });

    }
}
